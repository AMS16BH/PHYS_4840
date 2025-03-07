import numpy as np 

def error_order(x,h):

	x = x_func(x)

	for i in range(0,10):
		dx = np.gradient(x,x[i]-x[i-1])
		dxx = np.gradient(dx,dx[i]-dx[i-1])

	error = ((x + h*dx + ((h**2)/2)*dxx)-(x - h*dx - ((h**2)/2)*dxx))/2*h

	return error

def x_func(v):
	x_func = v**2
	return x_func

x = np.linspace(0,10,100)
h = np.ones(len(x))

print(error_order(x,h))
