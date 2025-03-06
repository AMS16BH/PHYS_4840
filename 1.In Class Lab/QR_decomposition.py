import math
import numpy as np 
import sys
import matplotlib.pyplot as plt 
from numpy import array,empty


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

#var1, var2 = np.loadtext(filename, usecols=(1,2), unpack=True)

#####
A = np.array([ [2, -1, 3,],\
			   [-1, 4, 5], 
			   [3,  5, 6] ],float)

eigenvector_1 =  np.array([-0.5774,\
						   -0.5774,\
						   0.5774],float)

LHS = np.dot(A, eigenvector_1)

## Bonus: Why doesn't this line work??
#LHS = A*eigenvector_1

RHS = -2.0*eigenvector_1

print("LHS:\n",LHS, "\n\nRHS:\n",RHS)


qr_decomposition(A)
print(f'{A}')


#1) Find Q and R
print(qr_decomposition(A))

#2) Confirm that Q is orthogonal

Q,R = qr_decomposition(A)
print(np.dot(Q,R))

#3) Confirm that R is upper triangular

print(R)
#4) Confirm that the matrix A introduced in eigenvalues.py can indeed be reconstructed by the dot product of matrices Q and R

