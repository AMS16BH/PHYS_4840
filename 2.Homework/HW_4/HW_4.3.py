

#### Equilibrium of a Suspended Beam ####

'''A rigid uniform beam of mass m = 10 kg and length L = 4 m is suspended
horizontally from two cables attached at different points. One cable is attached
2 meters from the left end, and the second cable is attached at the right end.
The beam also supports an additional mass M = 20 kg hanging 1 meter from
the left end.
Assume the system is in static equilibrium, meaning the sum of forces and
torques must be zero. Find the tension forces T1 and T2 in the two cables
and the horizontal and vertical reaction forces Rx and Ry at the left
end of the beam'''

'''
			|			|
			T1			T2
			|			|
	________0___________0
	|
	M
'''

### Step 1: Define the forces acting on the system ###

import numpy as np
from numpy import array,empty
import math

def gaussian_elimination(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    for i in range(n):
        # Partial pivoting: find the row with the largest absolute value in the current column
        max_row = i
        for k in range(i + 1, n):
            if abs(Ab[k][i]) > abs(Ab[max_row][i]):
                max_row = k

        # Swap the current row with the row with the largest absolute value
        Ab[[i, max_row]] = Ab[[max_row, i]]

        # Make the diagonal element 1
        if Ab[i][i] != 0:
            Ab[i] = Ab[i] / Ab[i][i]

        # Eliminate elements below the diagonal
        for k in range(n):
            if k != i:
                factor = Ab[k][i]
                Ab[k] = Ab[k] - factor * Ab[i]

    # Extract the solution
    x = Ab[:, n]
    return x


System_of_Equations= np.array([[1,0,0,0], [0,1,1,-1], [0,2,4,0], [0,2,-1,2]],float)
Total_Forces = np.array([0,294.3,392.4,196.2])

x = gaussian_elimination(System_of_Equations, Total_Forces)
print(f'Horizontal Reaction Force = {x[0]:.4f} N')
print(f'Vertical Reaction Force = {x[1]:.4f} N')
print(f'Cable One Tension = {x[2]:.4f} N')
print(f'Cable Two Tension = {x[3]:.4f} N')

A = System_of_Equations*x

N = len(A) 

L = np.array([[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)])

print("L looks like this: ", L)
U = np.transpose(System_of_Equations)
print("U looks like this: ", U)
for m in range(N):
    for i in range(m+1, N):        
        
        # Compute the multiplier for the current row operation
        L[i, m] = U[i, m] / U[m, m]
        
        # Subtract the appropriate multiple of the pivot row from the current row
        U[i, :] -= L[i, m] * U[m, :]

print('The lower triangular matrix L is:\n', L)
print('The upper triangular matrix U is:\n', U)



m, n = A.shape
Q = np.eye(m)
R = A.copy()

for j in range(n):
    v = R[j:, j]
    alpha = -np.sign(v[0]) * np.linalg.norm(v)
    e = np.zeros_like(v)
    e[0] = 1
    u = v - alpha * e
    u = u / np.linalg.norm(u)
    
    Q_j = np.eye(m)
    Q_j[j:, j:] -= 2 * np.outer(u, u)
    
    R = Q_j @ R
    Q = Q @ Q_j
        



