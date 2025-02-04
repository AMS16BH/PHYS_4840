
#####################################
#
# Class 5: Linear and Log + Plotting
# Author: Austin Smith
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('.github/function_lib')

# and import your functions library

import functions_lib as func


#____________________#


x = np.linspace(1, 100, 500)  # x values
y = 2.0*x**3.0
y_log = func.y(x)
x_log = func.x(y)



# (1) make a linear plot of y vs x

plt.plot(x,y, linestyle='-', color='blue', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.grid(True) ## turn on/off as needed
plt.show()

# (2) make a log-log plot of y vs x
plt.plot(x,y, linestyle='-', color='red', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True) ## turn on/off as needed
plt.show()

# (3) make a plot of log(x) vs log(y)
plt.plot(x_log,y_log, linestyle='-', color='red', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')
plt.grid(True) ## turn on/off as needed
plt.show()
