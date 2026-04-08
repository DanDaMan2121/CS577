import numpy as np
import matplotlib.pyplot as plt
# <!-- 2. We will continue with the *Yield Curves* problem from the class notes. Refer the notes for Class 4 (file: "CS677_Matplotlib_Subplots.html")
#    - Try to recreate the plot below that uses twin axes. While this plot may actually be more confusing than helpful, its a good exercise in Matplotlib control. -->
#    2. Assume that the data below shows the interest paid for a US Treasury bond for a certain contract length. The labels list shows the corresponding contract length per index position.
#       * 
# Labels = Contract leng
#       * h
# Y axis = interest p

# Plot the yield curves for both 2007 and 2020 as shown in the figure.aid

labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]
ax1 = plt.subplot()
ax1.plot(labels, july16_2007, 'blue')

# sets the y label for the first plotted line 
ax1.set_ylabel('2007', color='blue')
# sets the color of the ticks on the y axis to blue, and the font size to 15
ax1.tick_params(axis='y', colors='blue', labelsize=15)
# sets the "spine" on the left the graph to blue
ax1.spines['left'].set_color('blue')
# sets the label "2007" to the font size of 18
ax1.yaxis.label.set_fontsize(18)
# sets the width of the spine to 4
ax1.spines['left'].set_linewidth(4)

# creates a line to be plotted on the same plot as ax1
ax2 = ax1.twinx()
# plots ax2
ax2.plot(labels, july16_2020, 'red')
# sets the y label for the ax2 and changes it to red 
ax2.set_ylabel('2020', color='red')
# sets the label font size to 17
ax2.yaxis.label.set_fontsize(18)
# sets the "right" spine to red
ax2.spines['right'].set_color('red')
# sets the width of the "right" spine to 4
ax2.spines['right'].set_linewidth(4)
# sets the color to red, and the size of the tick labels to 15
ax2.tick_params(axis='y', colors='red', labelsize=15)

# sets the title of the graph
plt.title('July 16th Yield Curves')

plt.show()


