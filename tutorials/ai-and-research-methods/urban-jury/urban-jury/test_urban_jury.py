"""Offline checks: no credentials, network calls or model charges required."""
import contextlib
import io
import os
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import urban_jury as app


class UrbanJuryTests(unittest.TestCase):
    def test_only_selected_provider_needs_key(self):
        for provider, variable in app.KEYS.items():
            with self.subTest(provider=provider), patch.dict(os.environ, {variable: "test-key"}, clear=True):
                self.assertEqual(app.configuration(provider + "/example")["api_key"], "test-key")

    def test_missing_key_and_invalid_model(self):
        with patch.dict(os.environ, {}, clear=True):
            for model in ("openai/example", "anthropic/example", "deepseek/example", "example", "other/model", "ollama/"):
                with self.subTest(model=model), self.assertRaises(ValueError):
                    app.configuration(model)

    def test_ollama_is_local_and_keyless(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertNotIn("api_key", app.configuration("ollama/example"))
        with patch.dict(os.environ, {"OLLAMA_API_BASE": "https://remote.example"}, clear=True):
            with self.assertRaises(ValueError):
                app.configuration("ollama/example")

    def test_cost_requires_exact_pricing_and_complete_usage(self):
        client = SimpleNamespace(model_cost={}, completion_cost=Mock(return_value=0.001))
        usage = {"prompt_tokens": 20, "completion_tokens": 10}
        self.assertIsNone(app.cost_estimate(client, {}, "openai/example", usage)[0])
        client.completion_cost.assert_not_called()
        client.model_cost["example"] = {"input_cost_per_token": 0.01, "output_cost_per_token": 0.02}
        self.assertIsNone(app.cost_estimate(client, {}, "openai/example", {})[0])
        self.assertIsNone(app.cost_estimate(client, {"service_tier": "priority"}, "openai/example", usage)[0])
        self.assertEqual(app.cost_estimate(client, {}, "openai/example", usage)[0], 0.001)
        client.completion_cost.return_value = float("nan")
        self.assertIsNone(app.cost_estimate(client, {}, "openai/example", usage)[0])

    def test_mock_request_and_saved_record(self):
        response = Mock()
        response.model_dump.return_value = {"model": "example", "choices": [{"message": {"content": "A question"}}], "usage": {"prompt_tokens": 2, "completion_tokens": 3}}
        client = SimpleNamespace(completion=Mock(return_value=response))
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True), patch.dict(sys.modules, {"litellm": client}), contextlib.redirect_stdout(io.StringIO()):
            record = Path(directory) / "run.json"
            log = Path(directory) / "experiment-log.md"
            self.assertEqual(app.main(["--model", "ollama/example", "--log", str(log), "--record", str(record), "Question"]), 0)
            self.assertIn('"input_tokens": 2', record.read_text())
            self.assertIn('"question": "Question"', record.read_text())
            self.assertIn("Question", log.read_text(encoding="utf-8"))
            self.assertIn("A question", log.read_text(encoding="utf-8"))
            self.assertEqual(client.completion.call_args.kwargs["num_retries"], 0)
            self.assertNotIn("api_key", client.completion.call_args.kwargs)

    def test_log_appends_without_replacing_existing_notes(self):
        record = {"started_at_utc": "offline-test", "question": "Why?\n```", "response": "Answer\n```", "estimated_cost_usd": None}
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "experiment-log.md"
            log.write_text("Existing notes", encoding="utf-8")
            app.append_experiment(log, record)
            app.append_experiment(log, record)
            text = log.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("Existing notes"))
            self.assertEqual(text.count("## Recorded run:"), 2)
            self.assertIn("````\nWhy?\n```\n````", text)

    def test_errors_do_not_expose_provider_exception_text(self):
        class AuthenticationError(Exception):
            pass

        client = SimpleNamespace(
            completion=Mock(side_effect=AuthenticationError("secret-provider-details")),
            AuthenticationError=AuthenticationError,
        )
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True), patch.dict(sys.modules, {"litellm": client}), contextlib.redirect_stderr(errors), contextlib.redirect_stdout(io.StringIO()):
            log = Path(directory) / "errors.md"
            self.assertEqual(app.main(["--model", "ollama/example", "--log", str(log), "Question"]), 1)
            self.assertIn("AuthenticationError", log.read_text(encoding="utf-8"))
            self.assertNotIn("secret-provider-details", log.read_text(encoding="utf-8"))
        self.assertIn("Authentication failed", errors.getvalue())
        self.assertNotIn("secret-provider-details", errors.getvalue())

    def test_four_agents_are_isolated_and_errors_are_saved(self):
        import json
        calls = []
        console = io.StringIO()

        def completion(**kwargs):
            self.assertIn("Planned requests: 4", console.getvalue())
            self.assertIn("Possible cost:", console.getvalue())
            calls.append(json.loads(json.dumps(kwargs)))
            if len(calls) == 2:
                raise RuntimeError("private-provider-body")
            response = Mock()
            response.model_dump.return_value = {"model": "returned-model", "choices": [{"message": {"role": "assistant", "content": f"Reply {len(calls)}"}}], "usage": {"prompt_tokens": 7, "completion_tokens": 3}}
            return response

        client = SimpleNamespace(completion=completion)
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True), patch.dict(sys.modules, {"litellm": client}), contextlib.redirect_stdout(console), contextlib.redirect_stderr(io.StringIO()):
            background = Path(directory) / "background.txt"
            background.write_text("Shared evidence", encoding="utf-8")
            record = Path(directory) / "records.json"
            log = Path(directory) / "log.md"
            code = app.main(["--agents", "--model", "ollama/example", "--background-file", str(background), "--record", str(record), "--log", str(log), "Original question"])
            self.assertEqual(code, 1)
            self.assertEqual(len(calls), 4)
            self.assertEqual(len({call["messages"][0]["content"] for call in calls}), 4)
            self.assertEqual(len({call["messages"][1]["content"] for call in calls}), 1)
            for call in calls:
                self.assertEqual([m["role"] for m in call["messages"]], ["system", "user"])
                self.assertNotIn("Reply", str(call["messages"]))
            saved = json.loads(record.read_text(encoding="utf-8"))
            self.assertEqual(saved["question"], "Original question")
            self.assertEqual(saved["background"], "Shared evidence")
            self.assertEqual(saved["agents"][1]["error"]["type"], "RequestError")
            self.assertEqual(saved["agents"][0]["request"], calls[0])
            self.assertEqual(saved["agents"][0]["history"][-1]["content"], "Reply 1")
            self.assertEqual(saved["agents"][2]["history"][-1]["content"], "Reply 3")
            self.assertEqual(log.read_text(encoding="utf-8").count("## Recorded run:"), 4)
            self.assertNotIn("private-provider-body", record.read_text(encoding="utf-8"))

    def test_message_lists_and_dictionaries_are_not_shared(self):
        requests = app.build_requests("Question", "Background", True)
        requests[0][1][1]["content"] = "Changed"
        requests[0][1].append({"role": "assistant", "content": "Private"})
        self.assertNotEqual(requests[0][1][1], requests[1][1][1])
        self.assertEqual(len(requests[1][1]), 2)

    def test_dry_run_never_calls_provider(self):
        client = SimpleNamespace(completion=Mock())
        with patch.dict(sys.modules, {"litellm": client}), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(app.main(["--dry-run", "--model", "openai/example", "Question"]), 0)
        client.completion.assert_not_called()

    def test_missing_background_reports_specific_problem_without_request(self):
        client = SimpleNamespace(completion=Mock())
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.dict(sys.modules, {"litellm": client}), contextlib.redirect_stderr(errors):
            with self.assertRaises(SystemExit) as result:
                app.main(["--agents", "--model", "openai/example", "--background-file", str(Path(directory) / "missing.txt"), "Question"])
            self.assertEqual(result.exception.code, 2)
        self.assertIn("Background file not found:", errors.getvalue())
        client.completion.assert_not_called()

    def test_comparison_changes_only_system_instructions_and_saves_pair(self):
        import json
        calls = []

        def completion(**kwargs):
            calls.append(json.loads(json.dumps(kwargs)))
            response = Mock()
            response.model_dump.return_value = {"model": "snapshot", "choices": [{"message": {"role": "assistant", "content": f"Output {len(calls)}"}}], "usage": {"prompt_tokens": 8, "completion_tokens": 4}}
            return response

        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True), patch.dict(sys.modules, {"litellm": SimpleNamespace(completion=completion)}), contextlib.redirect_stdout(io.StringIO()):
            root = Path(directory)
            (root / "background.txt").write_text("Same evidence", encoding="utf-8")
            (root / "b.txt").write_text("Investigate planning assumptions and counterevidence.", encoding="utf-8")
            result = app.main(["--compare-agent", "urban_planner", "--instructions-b", str(root / "b.txt"), "--background-file", str(root / "background.txt"), "--model", "ollama/example", "--temperature", "0", "--max-tokens", "100", "--seed", "42", "--record", str(root / "pair.json"), "--log", str(root / "log.md"), "Same question"])
            self.assertEqual(result, 0)
            self.assertEqual(len(calls), 2)
            self.assertNotEqual(calls[0]["messages"][0], calls[1]["messages"][0])
            self.assertEqual(calls[0]["messages"][1], calls[1]["messages"][1])
            self.assertEqual(len(calls[1]["messages"]), 2)
            for key in ("model", "temperature", "max_tokens", "seed", "timeout", "num_retries", "api_base"):
                self.assertEqual(calls[0][key], calls[1][key])
            pair = json.loads((root / "pair.json").read_text(encoding="utf-8"))
            a, b = pair["agents"]
            self.assertEqual(a["comparison"]["id"], b["comparison"]["id"])
            self.assertEqual([a["comparison"]["version"], b["comparison"]["version"]], ["A", "B"])
            self.assertEqual(a["request"], calls[0])
            self.assertEqual(b["request"], calls[1])
            self.assertEqual(a["usage"]["completion_tokens"], 4)
            log = (root / "log.md").read_text(encoding="utf-8")
            self.assertIn("Output 1", log)
            self.assertIn("Output 2", log)
            self.assertIn("ordinary model variability", log)

    def test_comparison_rejects_empty_or_identical_instructions(self):
        import json
        baseline = json.loads(Path(app.__file__).with_name("agents.json").read_text(encoding="utf-8"))["agents"][0]["instructions"]
        for revised in ("", "  ", baseline):
            with self.subTest(revised=revised), self.assertRaises(ValueError):
                app.build_comparison("Question", "Background", "urban_planner", revised)


if __name__ == "__main__":
    unittest.main()
