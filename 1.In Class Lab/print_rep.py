
import subprocess


repo_path = "https://github.com/AMS16BH/PHYS_4840/tree/main/.github"


def run_git_command(command, cwd=repo_path):
	result = subprocess.run(command, cwd=repo_path, shell=True, capture_output=True, text=True)
	print(result.stdout)

	if result.stdeer:
		print("Error:", result.stderr)

run_git_command('get checkout main')

run_git_command('git pull origin main --rebase')

run_git_command('git add .')

commit_message = "Automated commit from Python script"

run_git_command(f'git commit -m "{commit_message}"')

run_git_command('git push origin main')



print(0.1+0.2)
print(repr(0.1+0.2))

######

from math import sqrt

x =1.0
y=1.0+(1e14)*sqrt(2)

answer_1 = 1e14*(y-x)
answer_2 = sqrt(2)

print("answer1: ", answer_1)
print("answer2: ", answer_2)

# WHat is the percent(%) difference between these answers?

#Larget number double-precision float 1.8e308 which is decimal rep
#Smallest number Python can represent is 2e-1022 (Saves a bit for the negative sign)

