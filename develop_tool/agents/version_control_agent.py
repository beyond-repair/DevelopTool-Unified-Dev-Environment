# develop_tool/agents/version_control_agent.
import subprocess

class VersionControlAgent:
    def __init__(self, repository_path):
        self.repository_path = repository_path

    def initialize_repository(self):
        subprocess.run(['git', 'init'], cwd=self.repository_path)

    def commit_changes(self, message):
        subprocess.run(['git', 'add', '.'], cwd=self.repository_path)
        subprocess.run(['git', 'commit', '-m', message], cwd=self.repository_path)

    def create_branch(self, branch_name):
        subprocess.run(['git', 'branch', branch_name], cwd=self.repository_path)

    def switch_branch(self, branch_name):
        subprocess.run(['git', 'checkout', branch_name], cwd=self.repository_path)
