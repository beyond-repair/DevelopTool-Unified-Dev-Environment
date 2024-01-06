import os
from pathlib import Path
class CI_CD_Agent:
    def setup_ci_cd_pipeline(self):
        import os
from pathlib import Path

# Correct path to environment.yml file
env_yml_path = Path(__file__).resolve().parent / 'environment.yml'

# Updated command with the correct path to the environment.yml file
print(f"Setting up CI/CD pipeline for automated building, testing, and deployment. Using environment file: {env_yml_path}")
