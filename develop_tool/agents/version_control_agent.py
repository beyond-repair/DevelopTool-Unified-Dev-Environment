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
            self.file_manager.add_changes()
            self.file_manager.commit_changes(message)
        except subprocess.CalledProcessError as e:
            print(f"Error committing changes: {e}")

    def create_branch(self, branch_name):
        try:
            self.file_manager.create_branch(branch_name)
        except subprocess.CalledProcessError as e:
            print(f"Error creating branch: {e}")

    def switch_branch(self, branch_name):
        try:
            self.file_manager.switch_branch(branch_name)
        except subprocess.CalledProcessError as e:
            print(f"Error switching branch: {e}")
