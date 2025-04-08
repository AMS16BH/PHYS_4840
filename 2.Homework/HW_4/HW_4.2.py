import math
import matplotlib.pyplot as plt

def gamma(z, iterations=12):
    if z == 0:
        return float('inf')
    if z < 0 and z == int(z):
        return float('inf')
    if z < 0:
        return math.pi / (math.sin(math.pi * z) * gamma(1 - z))
    if z > 100:
        return math.sqrt(2 * math.pi / z) * (z / math.e)**z
    result = 1
    for i in range(1, iterations + 1):
        result *= (i / (i + z))
    return result * (iterations**z) / z

x_values = [x / 10 for x in range(0, 5)]
y_values = [gamma(y) for y in range(2,4)]

plt.plot(x_values, y_values)
plt.xlabel('z')
plt.ylabel('Gamma(z)')
plt.title('Gamma Function')
plt.grid(True)
plt.show()
