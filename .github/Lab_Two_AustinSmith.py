#!/usr/local/Anaconda2023/bin


import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("users/austins/Desktop/PHYS_4840/NGC6341.dat")

filename = 'NGC6341.dat'

blue, green, red = np.loadtxt(filename,usecols=(8,14,26), unpack=True)

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

