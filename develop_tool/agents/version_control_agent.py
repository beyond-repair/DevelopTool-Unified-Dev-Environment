import subprocess
from file_manager import FileManager

class VersionControlAgent:
    def __init__(self, repository_path):
        self.repository_path = repository_path

    def initialize_repository(self):
        try:
            subprocess.run(['git', 'init'], cwd=self.repository_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error initializing repository: {e}")

    def commit_changes(self, message):
        try:
            subprocess.run(['git', 'add', '.'], cwd=self.repository_path, check=True)
            subprocess.run(['git', 'commit', '-m', message], cwd=self.repository_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error committing changes: {e}")

    def create_branch(self, branch_name):
        try:
            subprocess.run(['git', 'branch', branch_name], cwd=self.repository_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error creating branch: {e}")

    def switch_branch(self, branch_name):
        try:
            subprocess.run(['git', 'checkout', branch_name], cwd=self.repository_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error switching branch: {e}")
