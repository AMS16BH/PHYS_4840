import numpy as np
import time
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(...)
import my_functions_lib as lib

file_path = sys.path.append(...)

def f(x,t):
	return -x**3 + np.sin(t)

def second_order_RK(x0,t0,t_end,dt):

	t_values = np.arange(t0, t_end + dt, dt)
	x_values = np.zeros(len(t_values))
	x_values[0] = x0

	for i in range(1, len(t_values)):
		t = t_values[i - 1]
		x = x_values[i - 1]
		k1 = dt*f(x, t)
		k2 = dt*f(x+0.5*k1,t+0.5*dt)
		x_values[i] = x + k2

	return t_values, x_values

def fourth_order_RK(x0,t0,t_end,dt):

    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
    	t = t_values[i - 1]
    	x = x_values[i - 1]
    	k1 = dt*f(x, t)
    	k2 = dt*f(x+0.5*k1,t+0.5*dt)
    	k3 = dt*f(x+0.5*k2,t+0.5*dt)
    	k4 = dt*f(x+k3,t+dt)
    	x_values[i] = (k1+2*k2+2+k3+k4)/6

    return t_values, x_values

t0 = 0.0
t_end = 10.0
dt = 0.1
x0 = 0


fig, ax = plt.subplots(1,4)

t_values, x_values = second_order_RK(x0,t0,t_end,dt)
ax[0].plot(t_values, x_values)
ax[0].set_title('Python 2-OD')
t_values, x_values = fourth_order_RK(x0,t0,t_end,dt)
ax[1].plot(t_values, x_values)
ax[1].set_title('Python 4-OD')
t_values, x_values = np.loadtxt('...',unpack = True, skiprows=1,usecols=[0,1])
ax[2].plot(t_values, x_values)
ax[2].set_title('Fortran 2-OD')
t_values, x_values = np.loadtxt('...',unpack = True, skiprows=1,usecols=[0,1])
ax[3].plot(t_values, x_values)
ax[3].set_title('Fortran 4-OD')
plt.show()
