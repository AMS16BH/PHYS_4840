# import sunspots.txt

# Write a program that reads in the data and makes a graph of sunspots as function of time.

# MOdify your program to display on the first 1000 data points on the graph.

# Modify your program further to calculate and plot the running average of the data, defined by by the equation provided.
#  - r = 5
# - Have the program plot both the original data and the running average on the same graph, again over the range covered by the first 1000 data points.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import time
import os


print('test')


import subprocess


repo_path = os.getcwd()


def run_git_command(command, cwd=repo_path):
	result = subprocess.run(command, cwd=repo_path, shell=True, capture_output=True, text=True)
	print(result.stdout)

	if result.stderr:
		print("Error:", result.stderr)

run_git_command('git branch -M main')


run_git_command('git push -u origin main')

run_git_command('git remote add origin https://github.com/AMS16BH/PHYS-4840.git')

commit_message = "Automated commit from Python script"

run_git_command(f'git commit -m "{commit_message}"')

run_git_command('git push origin main')