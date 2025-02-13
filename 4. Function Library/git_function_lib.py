
import sys
import subprocess
import requests
import os

access_token = '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'
repo_path = '/d/users/austins/Desktop/PHYS_4840'

def authenticate_github(token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code == 200:
        print("Authentication successful!")
        print(response.json())
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

    COMMIT_MESSAGE = "Automated commit from Python Script."

    if not os.path.exists(repo_path):
        print("Error: Repository path does not exist!")
        return

    run_command("git add .",cwd=repo_path)
    run_command(f'git commit -m "{COMMIT_MESSAGE}"',cwd=repo_path)
    run_command("git push origin main", cwd=repo_path)

if __name__ == "__main__":
    upload_to_github()
#def run_git_command(command):
    #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #stdout, stderr = process.communicate()
    #return stdout, stderr, process.returncode

# Example usage:
#command = "git status"
#stdout, stderr, returncode = run_git_command(command)

#if returncode == 0:
    #print("Command executed successfully:")
    #print(stdout)
#else:
    #print(f"Error executing command: {command}")
    #print(stderr)

# Example for pushing changes
#command = "git push origin main"
#stdout, stderr, returncode = run_git_command(command)

#if returncode == 0:
    #print("Command executed successfully:")
    #print(stdout)
#else:
    #print(f"Error executing command: {command}")
    #print(stderr)