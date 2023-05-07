import matplotlib.pyplot as plt
import numpy as np

# create a Figure object
fig = plt.figure()

# create an Axes object
ax = fig.add_subplot(1, 1, 1)

# plot some data on the Axes object
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)

# set the title and axis labels
ax.set_title('Sine wave')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# show the plot
plt.show()
