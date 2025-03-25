import math
import numpy as np 
from math import tanh

def distance_modulus(distance):

	distance_modulus = 5*np.log10(distance/10)

	return distance_modulus

def f_with_numpy(x):
	## same as the above, but using tanh from numpy
	## rather than from math --- are they the same?
	fx = 1.0 + 0.5*np.tanh(2.0*x)
	return fx

def df_dx_analytical(x):
	dfdx = 1.0/(np.cosh(2.0*x)**2.0)
	return dfdx


###################################
def my_function(vector):
	a = vector[0]
	b = vector[1]
	c = vector[2]

	answer = np.linalg.norm(vector)

	return answer


vector = [10,11,12]
def normalize_vector(vector):
	answer = np.linalg.norm(vector)
	return answer, vector

# print("output of my function: ",\
# 	  normalize_vector(vector) )


# print( type(normalize_vector(vector)) )

def qr_decomposition(A):
    ## Computes the QR decomposition of matrix A using
    ## Gram-Schmidt orthogonalization.
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]  # Take column j of A
        for i in range(j):  # Subtract projections onto previous Q columns
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)  # Compute norm
        Q[:, j] = v / R[j, j]  # Normalize

    return Q, R

    ######

def pivot_matrix(data, index_col, col_col, value_col):
    pivoted_data = {}
    for row in data:
        index_val = row.get(index_col)
        col_val = row.get(col_col)
        value_val = row.get(value_col)

        if index_val is None or col_val is None or value_val is None:
            return None  # Cannot pivot with missing keys

        if index_val not in pivoted_data:
            pivoted_data[index_val] = {}

        if col_val in pivoted_data[index_val]:
             return None # Cannot pivot when the combination of index and column are not unique
        
        pivoted_data[index_val][col_val] = value_val
    return pivoted_data

def euler_method(f,x0,t0,t_end,dt):
    t_values = np.arange(t0,t_end+dt,dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        x_values[i] = x_values[i-1] + dt * f(x_values[i-1],t_values[i-1])

    return t_values,x_values
