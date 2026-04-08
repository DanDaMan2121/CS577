import numpy as np
import matplotlib.pyplot as plt
# 3. This problem will test your ability to generate subplots of varying sizes and types.
#    1. Data: generate a 1D array `x` comprising 100 equally spaced points between 0 and 10.
#    2. Using  `x` as input, generate y-axis data corresponding to the following three functions: $sin()$, $e^{()}$, and $\log(\cdot+1)$
#    3. Use the `subplot2grid()` method to reproduce the plot below as closely as possible. 
# x = np.linspace(0, 10, 100)



x = np.linspace(0, 10, 100)

# creates the figures to be plotted on
# 1x1 top left
fig1 = plt.subplot2grid((2, 2), (0, 0))
# 1x1 below the first one
fig2 = plt.subplot2grid((2, 2), (1, 0))
# 2x1 adjecent to the 2 above
fig3 = plt.subplot2grid((2, 2), (0, 1), rowspan=2) 

# input data into sin(x) to create a new array
ysin = np.sin(x)
# plot the data in the correct figure and color it blue
fig1.plot(x, ysin, 'blue')
# set the title and font size
fig1.set_title('Sine Wave', fontsize='10')

# input data into e^-x to create a new array
yexp = np.exp(-x)
# plot the data into its correct figure and color it green
fig2.plot(x, yexp, 'green')
# set the title and fontsize
fig2.set_title('Exponential Decay', fontsize='10')

# input data into log(x) to create a new array
ylog = np.log(x)
# if the values are 0 or below ignore set it to NaN
ylog[ylog <= 0] = np.nan 
# plot the data in the correct figure and color it red
fig3.plot(x, ylog, 'red')
# set the title and font size
fig3.set_title('Logarithmic Curve', fontsize='10')
# set the y ticks between 0 and 2.7 with a 0.5 step
fig3.set_yticks(np.arange(0, 2.7, 0.5))
# set the minimum window limit to -0.10
fig3.set_ylim(-0.10)

# Adjust the plots on the left to have more space between them
plt.subplots_adjust(hspace=0.3)
plt.show()
