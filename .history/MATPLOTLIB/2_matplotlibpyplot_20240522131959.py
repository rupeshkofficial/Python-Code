import matplotlib.pyplot as plt # now the pyplot package can be reffered as plt.
import numpy as np 

# plotting x and y
# plot() function is used to draw points or markers in a diagram
# There are 2 parameters for specifying points in the diagram i.e x-axis and y-axis

xpoints = np.array([1,8])
ypoints = np.array([3,10])
plt.plot(xpoints,ypoints)
plt.show()

# the x-axis is the horizontal
# the y-axis is the vertical



