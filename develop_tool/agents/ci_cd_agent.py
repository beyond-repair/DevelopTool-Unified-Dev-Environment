from develop_tool.agents.file_manager import copy_environment_file
from develop_tool.agents import file_manager
import os

class CI_CD_Agent:
    def setup_ci_cd_pipeline(self, file_manager):
        

        file_manager_instance = file_manager.FileManager()
        import sys
        self.environment_path = "DevelopTool-Unified-Dev-Environment/environment.yml"
        file_manager_instance.copy_file(self.environment_path, self.repository_path)
        self.environment_path = "DevelopTool-Unified-Dev-Environment/environment.yml"
        
        file_manager.copy_environment_file(self.environment_path, self.repository_path)

    def update_environment(self):
        import os
        import sys
        os.system(f"conda env update --file {self.environment_path} --name base")
