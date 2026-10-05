from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "learning-tutor" / "scripts" / "init_workspace.py"
spec = importlib.util.spec_from_file_location("init_workspace", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InitWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / "topic workspace"

    def init(self, **kwargs):
        kwargs.setdefault("workspace", self.workspace)
        kwargs.setdefault("topic", "Test topic")
        kwargs.setdefault("today", "2026-01-02")
        with redirect_stdout(io.StringIO()):
            return module.initialize(**kwargs)

    def test_creates_honest_resumable_workspace(self):
        created = self.init()
        self.assertEqual(len(created), 6)
        config = json.loads((self.workspace / ".learning/config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["schema_version"], 1)
        self.assertEqual(config["path"], "auto")
        self.assertEqual(config["evidence"], "auto")
        self.assertIn("No attempts", (self.workspace / ".learning/attempts.md").read_text(encoding="utf-8"))
        self.assertTrue((self.workspace / "notes/Overview.md").is_file())
        for path in created:
            self.assertNotIn("{{", path.read_text(encoding="utf-8"))
            self.assertFalse(path.read_bytes().startswith(b"\xef\xbb\xbf"))
        state = (self.workspace / ".learning/STATE.md").read_text(encoding="utf-8")
        for target in ("config.json", "plan.md", "memory.md", "attempts.md", "../notes/Overview.md"):
            self.assertTrue((self.workspace / ".learning" / target).exists())
        self.assertIn("2026-01-02", state)

    def test_rerun_preserves_edits_and_ignores_new_settings(self):
        self.init()
        state = self.workspace / ".learning/STATE.md"
        state.write_text("A learner-authored checkpoint\n", encoding="utf-8")
        before = {str(p.relative_to(self.workspace)): p.read_bytes() for p in self.workspace.rglob("*") if p.is_file()}
        self.assertEqual(self.init(topic="Changed", notes_format="none"), [])
        after = {str(p.relative_to(self.workspace)): p.read_bytes() for p in self.workspace.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_disabled_notes_have_no_output(self):
        self.assertEqual(len(self.init(notes_format="none")), 5)
        self.assertFalse((self.workspace / "notes").exists())
        config = json.loads((self.workspace / ".learning/config.json").read_text(encoding="utf-8"))
        self.assertFalse(config["notes"]["enabled"])
        self.assertNotIn("../notes/Overview.md", (self.workspace / ".learning/STATE.md").read_text(encoding="utf-8"))

    def test_obsidian_and_language_preferences(self):
        self.init(notes_format="obsidian", language="es", assessment_language="en", style="reference")
        config = json.loads((self.workspace / ".learning/config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["notes"]["format"], "obsidian")
        self.assertEqual(config["notes"]["style"], "reference")
        self.assertEqual(config["language"], "es")
        self.assertEqual(config["assessment_language"], "en")

    def test_existing_overview_refused_before_any_write(self):
        overview = self.workspace / "notes/Overview.md"
        overview.parent.mkdir(parents=True)
        overview.write_text("Keep my existing notes", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.init()
        self.assertFalse((self.workspace / ".learning").exists())
        self.assertEqual(overview.read_text(encoding="utf-8"), "Keep my existing notes")

    def test_dry_run_does_not_create_workspace(self):
        self.assertEqual(len(self.init(dry_run=True)), 6)
        self.assertFalse(self.workspace.exists())

    def test_unicode_and_yaml_escaping(self):
        topic = '概率: "条件" # α / β'
        self.init(topic=topic, workspace=self.root / "中文 学习目录")
        workspace = self.root / "中文 学习目录"
        config = json.loads((workspace / ".learning/config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["topic"], topic)
        overview = (workspace / "notes/Overview.md").read_text(encoding="utf-8")
        self.assertIn("title: " + json.dumps(topic, ensure_ascii=False), overview)
        self.assertFalse((workspace / "概率").exists())

    def test_topic_template_markers_are_not_interpreted(self):
        topic = "A {{date}} label"
        self.init(topic=topic)
        config = json.loads((self.workspace / ".learning/config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["topic"], topic)
        self.assertIn(topic, (self.workspace / "notes/Overview.md").read_text(encoding="utf-8"))

    def test_invalid_inputs_do_not_write(self):
        for values in ({"topic": ""}, {"topic": "line\nbreak"}, {"today": "not-a-date"}, {"style": "invalid"}, {"notes_format": "invalid"}):
            with self.subTest(values=values), self.assertRaises(ValueError):
                self.init(**values)
            self.assertFalse(self.workspace.exists())

    def test_explicit_workspace_is_required_by_cli(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--topic", "Test"], cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--workspace", result.stderr)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_tutor_skill_works_without_repository_or_sibling(self):
        isolated = self.root / "installed" / "learning-tutor"
        shutil.copytree(SCRIPT.parent.parent, isolated, ignore=shutil.ignore_patterns("__pycache__"))
        result = subprocess.run([
            sys.executable, str(isolated / "scripts/init_workspace.py"),
            "--workspace", str(self.workspace), "--topic", "Standalone", "--notes-format", "none",
        ], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.workspace / ".learning/STATE.md").is_file())
        self.assertFalse((isolated.parent / "study-notes").exists())

    def test_symlink_escape_is_refused(self):
        self.workspace.mkdir()
        outside = self.root / "outside"
        outside.mkdir()
        try:
            (self.workspace / "notes").symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"Directory symlinks unavailable: {exc}")
        with self.assertRaises(ValueError):
            self.init()
        self.assertFalse((self.workspace / ".learning").exists())
        self.assertEqual(list(outside.iterdir()), [])

    def test_parent_file_conflict_is_refused_before_write(self):
        self.workspace.mkdir()
        (self.workspace / "notes").write_text("existing file", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.init()
        self.assertFalse((self.workspace / ".learning").exists())


if __name__ == "__main__":
    unittest.main()
