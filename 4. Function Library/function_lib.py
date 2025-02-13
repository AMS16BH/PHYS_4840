import math
import numpy as np 

def distance_modulus(distance):

	distance_modulus = 5*np.log10(distance/10)

	return distance_modulus

