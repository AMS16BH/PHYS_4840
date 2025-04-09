
#################  Question 1:

import numpy as np
import matplotlib.pyplot as plt

def square_wave(t):
	return np.where(t%1 < 0.5, 1, -1)

def Q(t,RC):
	return square_wave(t)*(1-np.exp(-t/RC))

def voltage_out(RC,t):

	V_Out = []
	V = 0

	for i in t:
		V_Out.append(V)
		k1 = dt * Q(i,RC)
		k2 = dt * Q(i+0.5*k1,RC+0.5+dt)
		k3 = dt * Q(i+0.5*k2,RC+0.5+dt)
		k4 = dt * Q(i+k3,RC+dt)
		V += (k1 + 2 * k2 + 2 * k3 + k4)/6
	return V_Out

dt = 500
t = np.linspace(0, 10.0, dt)
RC = [0.01, 0.1, 1.0]
A = 1.0
T = 2 * np.pi
n_terms = 10


plt.plot(t, voltage_out(RC[0], t))
plt.plot(t, voltage_out(RC[1], t))
plt.plot(t, voltage_out(RC[2], t))
plt.grid(True)
plt.show()

######################################
##### Question(s) 2 and 3
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
t_values, x_values = np.loadtxt(...,unpack = True, skiprows=1,usecols=[0,1])
ax[2].plot(t_values, x_values)
ax[2].set_title('Fortran 2-OD')
t_values, x_values = np.loadtxt(...,unpack = True, skiprows=1,usecols=[0,1])
ax[3].plot(t_values, x_values)
ax[3].set_title('Fortran 4-OD')
plt.show()

########################

# Question 4 & 5
'''
Python Second-Order RK = 0.022705307928845286
Python Fourth-Order RK = 0.04493305995129049

Running RK4.exe...100 time steps
 Integration complete. Results saved to rk4_results.dat
Compilation time: .012122233 seconds
Execution time: .008939918 seconds

Running RK4.exe...10,000 time steps
 Integration complete. Results saved to rk4_results.dat
Compilation time: .062746556 seconds
Execution time: .022808982 seconds

Running RK2.exe...100 time steps
 Integration complete. Results saved to rk2_results.dat
Compilation time: .061417671 seconds
Execution time: .004015211 seconds

Running RK2.exe...10,000 time step
 Integration complete. Results saved to rk2_results.dat
Compilation time: .056531487 seconds
Execution time: .023005600 seconds
bash-5.1$ 

At 10,000 time steps python RK2 is faster than fortran RK2, but fortran RK4 is twice as fast and comparable in speed to RK2 in python.

'''
import numpy as np
import time
import matplotlib.pyplot as plt
import os
import sys
import timeit

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
dt = 0.001
x0 = 0


fig, ax = plt.subplots(1,2)

start_2 = timeit.default_timer()
t_values, x_values = second_order_RK(x0,t0,t_end,dt)
ax[0].plot(t_values, x_values)
ax[0].set_title('Python 2-OD')
stop_2 = timeit.default_timer()

start_4 = timeit.default_timer()
t_values, x_values = fourth_order_RK(x0,t0,t_end,dt)
ax[1].plot(t_values, x_values)
ax[1].set_title('Python 4-OD')
stop_4 = timeit.default_timer()


print('Time: ', stop_2 - start_2)
print('Time: ', stop_4 - start_4)

plt.show()

######
#6: Makes the file identified executable in the cmd terminal but requires a #!/usr/bin/python## at the top.


