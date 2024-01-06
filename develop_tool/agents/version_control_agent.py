import subprocess
import file_manager

class VersionControlAgent:
    def __init__(self, repository_path, file_manager):
        self.repository_path = repository_path

    def initialize_repository(self):
        try:
            subprocess.run(['git', 'init'], cwd=self.repository_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error initializing repository: {e}")

    def copy_file_to_directory(self, file_manager):
        file_manager_instance = file_manager.FileManager()
        file_manager_instance.copy_file(self.environment_path, self.repository_path)

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
