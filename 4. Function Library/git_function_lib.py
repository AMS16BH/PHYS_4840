
import sys
import subprocess
import requests
import os

access_token = input("Access_Token:")
repo_path = '/d/users/austins/Desktop/PHYS_4840'
github_username = "AMS16BH"
github_repo = "PHYS_4840"
COMMIT_MESSAGE = "Automated commit from Python Script."


def authenticate_github(token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get("https://github.com/AMS16BH/PHYS-4840", headers=headers)
    if response.status_code == 200:
        print("Authentication successful!")
    else:
        print(f"Authentication failed. Status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    github_token = access_token 
    authenticate_github(github_token)


def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def upload_to_github():

    if not os.path.exists(repo_path):
        print("Error: Repository path does not exist!")
        return

    print("\nFetching latest changes from GitHUb...")
    run_command("git pull origin main --rebase", cwd=repo_path)

    print("\nAdding changes to Git...")
    run_command("git add .",cwd=repo_path)

    print("\nCommitting changes...")
    run_command(f'git commit -m "{COMMIT_MESSAGE}"',cwd=repo_path)

    print("\nPushing changes to GitHub...")
    run_command("git push origin main", cwd=repo_path)


if __name__ == "__main__":
    upload_to_github()
