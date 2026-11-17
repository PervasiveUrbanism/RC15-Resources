"""UI adapter checks with mocked providers; no Gradio install needed for these tests."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import app


def prepared(rounds=0, roles=None):
    return app.plan("Question", "Background", "Jury", roles or app.ROLES[:2], "ollama", "ollama/example",
                    rounds, False, 100, None, None, None, None, True)


def client(answer="Mock answer", fail=False):
    response = Mock()
    response.model_dump.return_value = {"model": "example", "choices": [{"message": {"role": "assistant", "content": answer}, "finish_reason": "stop"}],
                                       "usage": {"prompt_tokens": 5, "completion_tokens": 4}}
    completion = Mock(side_effect=RuntimeError("private-server-error")) if fail else Mock(return_value=response)
    return SimpleNamespace(completion=completion)


class InterfaceTests(unittest.TestCase):
    def tearDown(self):
        app.CONTROLS.clear()

    def test_preview_counts_selected_roles_and_moderator(self):
        config = prepared(2)
        self.assertEqual(config["planned_calls"], 6)
        self.assertEqual(len(config["requests"]), 2)
        self.assertEqual([agent for agent, _ in config["requests"]], app.ROLES[:2])
        self.assertEqual(len(prepared(0)["requests"]), 2)
        self.assertEqual(app.method_view()["discussion_instructions"].keys(), {"1", "2"})

    def test_failed_connections_are_recorded_without_secrets(self):
        fake = client(fail=True)
        with tempfile.TemporaryDirectory() as directory, patch.object(app, "ROOT", Path(directory)), patch.dict(sys.modules, {"litellm": fake}), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            updates = list(app.start(prepared(), "test"))
            self.assertFalse(updates[-1][-1])
            session = app.CONTROLS["test"].snapshot
            self.assertEqual(session["status"], "stopped")
            transcript = app.transcript_html(session)
            self.assertIn("R0-A1", transcript)
            self.assertIn("Model request failed", transcript)
            self.assertNotIn("private-server-error", json.dumps(session))
            exports = app.export_session("test")
            self.assertEqual(len(exports), 3)
            for file in exports:
                self.assertTrue(Path(file).exists())
            exported = json.loads(Path(exports[0]).read_text(encoding="utf-8"))
            self.assertEqual(len(exported["rounds"][0]["calls"]), 2)

    def test_intervention_is_identical_and_snapshot_unchanged(self):
        fake = client()
        with tempfile.TemporaryDirectory() as directory, patch.object(app, "ROOT", Path(directory)), patch.dict(sys.modules, {"litellm": fake}), contextlib.redirect_stdout(io.StringIO()):
            stream = app.start(prepared(1), "test")
            for update in stream:
                if update[0].startswith("**paused**"):
                    self.assertIn("Continuing", app.intervene("test", "Investigate counterevidence."))
            session = app.CONTROLS["test"].snapshot
            self.assertEqual(session["status"], "complete")
            self.assertEqual(session["interventions"][0]["message_id"], "I1")
            self.assertEqual(session["interventions"][0]["text"], "Investigate counterevidence.")
            for call in session["rounds"][1]["calls"]:
                self.assertIn("Investigate counterevidence.", str(call["request"]["messages"]))
            self.assertNotIn("Investigate counterevidence", str(session["rounds"][1]["snapshot"]))
            self.assertEqual(fake.completion.call_count, 4)

    def test_stop_while_paused_preserves_prior_round(self):
        fake = client()
        with tempfile.TemporaryDirectory() as directory, patch.object(app, "ROOT", Path(directory)), patch.dict(sys.modules, {"litellm": fake}), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            for update in app.start(prepared(1), "test"):
                if update[0].startswith("**paused**"):
                    app.stop_run("test")
            session = app.CONTROLS["test"].snapshot
            self.assertEqual(session["status"], "stopped")
            self.assertEqual(len(session["rounds"]), 1)
            self.assertEqual(fake.completion.call_count, 2)

    def test_generated_markup_is_escaped(self):
        session = {"rounds": [{"number": 0, "calls": [{"message_id": "R0-A1", "agent_id": "role", "response": "<script>bad</script>", "full_response": {}}]}]}
        self.assertNotIn("<script>", app.transcript_html(session))

    def test_openai_key_is_used_but_never_saved(self):
        fake = client()
        secret = "offline-placeholder-not-a-real-key"
        config = app.plan("Question", "Background", "Jury", app.ROLES[:1], "openai", "openai/example",
                          0, False, 100, None, None, None, None, True, secret)
        self.assertNotIn(secret, json.dumps(config))
        self.assertIn("configured", config["configuration"])
        with tempfile.TemporaryDirectory() as directory, patch.object(app, "ROOT", Path(directory)), patch.dict(sys.modules, {"litellm": fake}), patch.object(app, "request_once", wraps=app.request_once):
            # Supply an exact-price map with no entry so no estimate is fabricated.
            fake.model_cost = {}
            with contextlib.redirect_stdout(io.StringIO()):
                list(app.start(config, "key-test", secret))
            self.assertEqual(fake.completion.call_args.kwargs["api_key"], secret)
            session = app.CONTROLS["key-test"].snapshot
            self.assertNotIn(secret, json.dumps(session))
            for file in app.export_session("key-test"):
                self.assertNotIn(secret, Path(file).read_text(encoding="utf-8-sig"))
