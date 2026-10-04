"""Claim-capped surface checks. Does not execute agents, git, conda, or network."""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class SurfaceTest(unittest.TestCase):
    def test_archived_banner(self):
        text = (ROOT / "ARCHIVED.md").read_text(encoding="utf-8")
        self.assertIn("Archived", text)

    def test_readme_claim_cap(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("ARCHIVE QUEUE", text)
        self.assertIn("CLAIM       0", text)
        self.assertIn("historical preserved body", text.lower())

    def test_placeholder_token_not_a_credential(self):
        text = (ROOT / "develop_tool" / "main.py").read_text(encoding="utf-8")
        self.assertIn("your_github_token", text)
        self.assertNotIn("ghp_", text)

    def test_constructor_mismatch_is_documented(self):
        main = (ROOT / "develop_tool" / "main.py").read_text(encoding="utf-8")
        agent = (ROOT / "develop_tool" / "agents" / "version_control_agent.py").read_text(encoding="utf-8")
        self.assertIn("VersionControlAgent(repo_path)", main)
        self.assertIn("def __init__(self, repository_path, file_manager)", agent)
        claim = (ROOT / "CLAIM_STATUS.md").read_text(encoding="utf-8")
        self.assertIn("constructor mismatch", claim)

    def test_push_workflows_do_not_mutate(self):
        for name in ("setup.yml", "conda-env-update.yml", "python-package-conda.yml"):
            text = (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")
            self.assertNotIn("git push", text)
            self.assertIn("workflow_dispatch", text)
            self.assertNotIn("branches:", text)


if __name__ == "__main__":
    unittest.main()
