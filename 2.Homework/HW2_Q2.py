#2. Plot the function y = x4 over the domain -100 to 100 on a linear grid and on a log-log grid. Plot
#   the log(base10) of this function on a linear grid. Combine these to make one single, three-panel
#   figure, using different color and line/marker combinations for each panel. Use grid lines, 
#   reasonable font sizes for labels, and make the panel dimensions demonstrative of the differences between the three plots.

import matplotlib.pyplot as plt
import sys
import numpy as np
import math

def question_2():
	x = np.linspace(-100,101).astype(int)
	y = x**4
	

	
	fig, ax1 = plt.subplots()

	ax1.plot(x,y,'b')
	
	ax2 = ax1.twinx()
	ax2.set_yscale('log')


	ax2.plot(x,y)

	
	


	plt.show()

question_2()
