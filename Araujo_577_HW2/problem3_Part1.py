import numpy as np
import matplotlib.pyplot as plt

m = np.arange(0, 11)
c = 3 * (10 ** 8)
print(m)
e = m * (c ** 2)
print(e)


# defines style
plt.style.use('seaborn-v0_8-whitegrid')

# creates an axes to be shown on the plot
ax = plt.subplot()
ax.plot(e, 'r', linewidth='4')

# modifies the graphs' border
for spine in ax.spines.values():
    spine.set_color('black')

# defines the x label
plt.xlabel('Mass in grams')

# defines the y label
plt.ylabel('Eneregy in Joules')

# defined the title
plt.title('$E = mc^2$')

# defines the x limits on the window view
plt.xlim(0, 10)

# creates the ticks for box axis
ax.tick_params(which='both', axis='both', length=4)

plt.show()