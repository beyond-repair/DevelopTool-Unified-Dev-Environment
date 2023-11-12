import requests

class ProjectManagementAgent:
    def __init__(self, repo_owner, repo_name, token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_issue(self, title, body):
        url = f"{self.base_url}/issues"
        data = {"title": title, "body": body}
        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 201:
            print("Issue created successfully.")
        else:
            print(f"Failed to create issue. Status code: {response.status_code}")
