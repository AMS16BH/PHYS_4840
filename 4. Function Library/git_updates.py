import subprocess
import sys


repo_path = "/d/users/austins/Desktop/PHYS_4840"


def run_git_command(command, cwd=repo_path):
	result = subprocess.run(command, cwd=repo_path, shell=True, capture_output=True, text=True)
	print(result.stdout)
	if result.stderr:
		print(f"Error:, {result.stderr}")

run_git_command('git remote -v')

run_git_command('git remote remove origin')

run_git_command('git remote add origin https://github.com/AMS16BH/PHYS_4840.git')


run_git_command('git push -u origin main')

