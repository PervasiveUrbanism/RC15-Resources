"""Offline verification of round boundaries, snapshots and stopping limits."""
from copy import deepcopy
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from discussion import run_discussion, MODERATOR_SECTIONS, validate_summary
from urban_jury import build_requests


class DiscussionTests(unittest.TestCase):
    def run_case(self, *, rounds=2, cap=12, fail=None, log_failure=False, budget=None, model="ollama/example", moderator=False):
        self.calls = []
        self.logged = []

        def request(client, options, agent, messages, question, background, generation):
            self.calls.append(deepcopy(messages))
            index = len(self.calls)
            answer = None if index == fail else f"UNIQUE_REPLY_{index}_END"
            if agent == "moderator":
                answer = json.dumps({key: [{"text": "Interpretation", "references": ["R0-A1", "R1-A2"]}] for key in MODERATOR_SECTIONS})
            return {"agent_id": agent, "response": answer,
                    "request": {"model": options["model"], "messages": deepcopy(messages)},
                    "error": {"type": "TestError"} if index == fail else None,
                    "history": deepcopy(messages) + ([{"role": "assistant", "content": answer}] if answer else []),
                    "estimated_cost_usd": None,
                    "full_response": {"choices": [{"finish_reason": "stop"}]}}

        def append(path, record):
            if log_failure:
                raise OSError("mock write failure")
            self.logged.append(deepcopy(record))

        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            path = Path(directory) / "session.json"
            result = run_discussion(None, {"model": model}, build_requests("Question", "Background", True),
                                    "Question", "Background", {"max_tokens": 800}, rounds, cap,
                                    budget, Path(directory) / "log.md", path, request, append, moderator=moderator)
            self.session = json.loads(path.read_text(encoding="utf-8"))
            return result

    def test_fixed_snapshots_and_separate_histories(self):
        self.assertEqual(self.run_case(), 0)
        self.assertEqual(len(self.calls), 12)
        self.assertEqual([r["number"] for r in self.session["rounds"]], [0, 1, 2])
        for i in range(4):
            self.assertNotIn("UNIQUE_REPLY_", str(self.calls[i]))
            round_one = self.calls[4+i]
            self.assertEqual(round_one[-1], self.calls[4][-1])
            for n in range(1, 5):
                self.assertIn(f"UNIQUE_REPLY_{n}_END", round_one[-1]["content"])
            for n in range(5, 9):
                self.assertNotIn(f"UNIQUE_REPLY_{n}_END", str(round_one))
            own_assistants = [m["content"] for m in round_one if m["role"] == "assistant"]
            self.assertEqual(own_assistants, [f"UNIQUE_REPLY_{i+1}_END"])
            self.assertEqual(self.calls[8+i][-1], self.calls[8][-1])
        self.assertEqual(self.session["rounds"][1]["snapshot"][0]["response"], "UNIQUE_REPLY_1_END")
        self.assertEqual(len(self.logged), 12)
        self.assertEqual(self.session["status"], "complete")

    def test_failure_finishes_round_but_prevents_next(self):
        self.assertEqual(self.run_case(fail=2), 1)
        self.assertEqual(len(self.calls), 4)
        self.assertEqual(len(self.session["rounds"]), 1)
        self.assertEqual(self.session["rounds"][0]["status"], "incomplete")

    def test_call_cap_preserves_partial_round(self):
        self.assertEqual(self.run_case(cap=5), 1)
        self.assertEqual(len(self.calls), 5)
        self.assertEqual(len(self.session["rounds"][1]["calls"]), 1)

    def test_log_failure_stops_immediately_with_json_saved(self):
        self.assertEqual(self.run_case(log_failure=True), 1)
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(len(self.session["rounds"][0]["calls"]), 1)

    def test_unknown_hosted_budget_bound_prevents_charges(self):
        self.assertEqual(self.run_case(budget=1, model="openai/example"), 1)
        self.assertEqual(len(self.calls), 0)

    def test_one_round_caps_at_eight_calls(self):
        self.assertEqual(self.run_case(rounds=1), 0)
        self.assertEqual(len(self.calls), 8)

    def test_moderator_sees_complete_identified_transcript(self):
        self.assertEqual(self.run_case(cap=13, moderator=True), 0)
        self.assertEqual(len(self.calls), 13)
        self.assertEqual(self.session["moderator"]["status"], "complete")
        transcript = self.session["moderator"]["transcript"]
        self.assertEqual(len(transcript), 12)
        self.assertEqual(transcript[0]["message_id"], "R0-A1")
        self.assertEqual(transcript[-1]["message_id"], "R2-A4")
        for item in transcript:
            self.assertIn(item["response"], self.calls[-1][-1]["content"])
            self.assertEqual(len(item["request_message_ids"]), len(item["request"]["messages"]))
        self.assertEqual(self.session["moderator"]["call"]["message_id"], "MOD-1")
        self.assertEqual(len(self.session["rounds"]), 3)

    def test_moderator_not_run_for_incomplete_discussion(self):
        self.assertEqual(self.run_case(cap=13, moderator=True, fail=2), 1)
        self.assertEqual(len(self.calls), 4)
        self.assertNotIn("moderator", self.session)

    def test_moderator_respects_overall_call_cap(self):
        self.assertEqual(self.run_case(cap=12, moderator=True), 1)
        self.assertEqual(len(self.calls), 12)
        self.assertNotIn("moderator", self.session)

    def test_moderator_references_are_checked_without_rewriting(self):
        summary = {key: [] for key in MODERATOR_SECTIONS}
        summary["major_arguments"] = [{"text": "Unsupported source R9-A9", "references": ["R0-A1"]}]
        self.assertIsNotNone(validate_summary(json.dumps(summary), {"R0-A1"})[1])
        summary["major_arguments"][0] = {"text": "Interpretation", "references": ["R9-A9"]}
        self.assertIsNotNone(validate_summary(json.dumps(summary), {"R0-A1"})[1])
        self.assertIsNotNone(validate_summary("not JSON", {"R0-A1"})[1])
