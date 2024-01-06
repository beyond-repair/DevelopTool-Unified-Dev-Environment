class CI_CD_Agent:
    def setup_ci_cd_pipeline(self, file_manager):
        from file_manager import FileManager

        file_manager_instance = file_manager.FileManager()
        import sys
        self.environment_path = "DevelopTool-Unified-Dev-Environment/DevelopTool-Unified-Dev-Environment/environment.yml"
        
        file_manager_instance.copy_file_to_directory(self.environment_path)
        self.update_environment()

    def update_environment(self):
        import os
        import sys
        os.system(f"conda env update --file {self.environment_path} --name base")
