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

ax = plt.figure().add_subplot(projection='3d')

x = blue - red 
y = blue


# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x, y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')

# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('Color: B-R')
ax.set_ylabel('Magnitude: B')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()



