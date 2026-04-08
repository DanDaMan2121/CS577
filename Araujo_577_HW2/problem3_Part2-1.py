import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


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

ax.set_yscale('log')

# defines the x label
# plt.xlabel('Mass in grams')

# defines the x label
plt.xlabel('Eneregy in Joules')

# defined the title
plt.title('$E = mc^2$')

# defines the x limits on the window view
plt.xlim(0, 10)

# creates the y axis ticks
ax.set_yticks(np.linspace((10 ** 17), (10 ** 18), 10))

# sets y axis ticks
ax.tick_params(which='both')
ax.tick_params(which='major', length=3)
ax.tick_params(which='minor', length=3)


# removes the x axis grid-lines
plt.grid(False, which='major', axis='x')

# shows y axis grid-lines for minior ticks
plt.grid(True, 'minor', axis='y')

plt.show()