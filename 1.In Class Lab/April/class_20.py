import numpy as np
import matplotlib.pyplot as plt
import sys

#Constants

g , l , m = 9.81 , 0.60 , 1  # m/s^2 , meters , kg
dt = 0.01
t_max = 10.0
t = np.arange(0.0,t_max,dt)

theta1 = np.radians(90)
theta2 = np.radians(90)
omega1 = 0.0
omega2 = 0.0

r0 = np.array([theta1, theta2, omega1, omega2])

def equations(r):
    
    theta1, theta2, omega1, omega2 = r
    delta_theta = theta2 - theta1

    # Define the four equations for the system
    ftheta1 = omega1
    ftheta2 = omega2

    # The derivatives of omega1 and omega2
    denom1 = (2 * m * l ** 2)
    denom2 = (m * l ** 2)

    fomega1 = (-g * (2 * m) * np.sin(theta1) - m * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(delta_theta) * m * (omega2 ** 2 * l + omega1 ** 2 * l * np.cos(delta_theta))) / denom1

    fomega2 = (2 * np.sin(delta_theta) * (omega1 ** 2 * l * m + g * m * np.cos(theta1) + omega2 ** 2 * l * m * np.cos(delta_theta))) / denom2

    return np.array([ftheta1, ftheta2, fomega1, fomega2])

def rk4_step(r, dt):
    k1 = dt * equations(r)
    k2 = dt * equations(r + 0.5 * k1)
    k3 = dt * equations(r + 0.5 * k2)
    k4 = dt * equations(r + k3)
    return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

R = np.zeros((len(t), 4))
R[0] = r0

for i in range(1, len(t)):
    R[i] = rk4_step(R[i - 1], dt)

# Extract angles and angular velocities
theta1_vals, theta2_vals, omega1_vals, omega2_vals = R.T

# Convert to Cartesian coordinates for visualization
x1 = l * np.sin(theta1_vals)
y1 = -l * np.cos(theta1_vals)
x2 = x1 + l * np.sin(theta2_vals)
y2 = y1 - l * np.cos(theta2_vals)

# Save data
np.savetxt("double_pendulum_data_test.txt", np.column_stack([t, x1, y1, x2, y2]),
           header="time x1 y1 x2 y2", comments="")