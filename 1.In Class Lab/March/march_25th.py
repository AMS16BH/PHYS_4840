import numpy as np
import time
import matplotlib.pyplot as plt
import os
import sys

sys.path.append('/d/users/austins/Desktop/PHYS_4840/4. Function Library/')
import my_functions_lib as lib

def f(x,t):
	return -x**3 + np.sin(t)

def second_order_RK(a,b,N,x):

    h = (b-a)/N
    tpoints = np.arange(a,b,h)
    xpoints = []

    for t in tpoints:
        xpoints.append(x)
        k1 = h*f(x,t)
        k2 = h*f(x+0.5*k1,t+0.5*h)
        x += k2

    return xpoints, tpoints

def fourth_order_RK(a,b,N,x):

    h = (b-a)/N
    tpoints = np.arange(a,b,h)
    xpoints = []

    for t in tpoints:
        xpoints.append(x)
        k1 = h*f(x,t)
        k2 = h*f(x+0.5*k1,t+0.5*h)
        k3 = h*f(x+0.5*k2,t+0.5*h)
        k4 = h*f(x+k3,t+h)
        x += (k1+2*k2+2+k3+k4)/6

    return xpoints, tpoints
	
a = 0.0
b = 10.0
N =100
x = 0.0

####Euler's Method ####

t0 = a
t_end = 9.0
dt = 1.0
x0 = 0

fig, ax = plt.subplots(1,3)


ax[0].plot(second_order_RK(a,b,N,x))
ax[0].set_title('2nd Order')
ax[1].plot(fourth_order_RK(a,b,N,x))
ax[1].set_title('4th Order')
ax[2].plot(lib.euler_method(f,x0,t0,t_end,dt))
ax[2].set_title('Euler Method')
plt.show()
