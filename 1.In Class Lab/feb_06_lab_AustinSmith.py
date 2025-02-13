#!/usr/local/Anaconda2023/bin


import numpy as np
import matplotlib.pyplot as price_list
import sys

sys.path.append("/d/users/austins/Desktop/PHYS_4840/DATA/")

import my_functions_lib as mfl

filename = 'NGC6341.dat'

blue, green, red = np.loadtxt(filename,usecols=(8,14,26), unpack=True)
