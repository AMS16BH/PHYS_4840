#!/usr/local/Anaconda2023/bin


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import time

sys.path.append("users/austins/Desktop/PHYS_4840/NGC6341.dat")

filename = 'NGC6341.dat'

###################################################
#
# testing np.loadtxt()
#
###################################################

start_numpy = time.perf_counter()

blue, green, red = np.loadtxt(filename,usecols=(8,14,26), unpack=True)

end_numpy = time.perf_counter()

print('Time to run loadtxt version: ',end_numpy-start_numpy, ' seconds')

print("len(green): ", len(green))


###################################################
#
# testing custom parser
#
###################################################


blue,green, red = [], [], []

start_parser = time.perf_counter()


with open(filename,'r') as file:
	for line in file:
		if line.startswith('#'):
			continue

		columns = line.split()

		blue.append(float(columns[8]))
		green.append(float(columns[14]))
		red.append(float(columns[26]))

blue=np.array(blue)
green=np.array(green)
red=np.array(red)


end_parser  = time.perf_counter()

print('Time to run custom parser version: ', end_parser-start_parser, ' seconds')

print("len(green):", len(green))

###################################################
#
# testing pandas
#
###################################################
start_pandas = time.perf_counter()

df = pd.read_csv(filename, delim_whitespace=True, comment='#', header=None, skiprows=54)

blue = df.iloc[:, 8]   # Column 9 
green = df.iloc[:, 14]  # Column 15 
red = df.iloc[:, 26]   # Column 27 

blue = blue.to_numpy()
green = green.to_numpy()
red = red.to_numpy()

end_pandas  = time.perf_counter()

print('Time to run pandas version: ', end_pandas-start_pandas, ' seconds')

print("len(green):", len(green))


###################################################
#
# I-V Plot
#
###################################################

magnitude = blue #y-axis
color = blue - red #x-axis

fig, ax = plt.subplots()

plt.title("Hubble Space Telescope Data for the Globular CLuster NGC6341")

ax.scatter(color, magnitude,s=0.1,c="black")
plt.tight_layout()


ax.set_xlim(-2, 5)
ax.set_ylim(25, 14)
ax.set_xlabel('Color: B-R')
ax.set_ylabel('Magnitude: B')

plt.show()

