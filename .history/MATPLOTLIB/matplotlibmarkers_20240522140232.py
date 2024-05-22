# You can use argument marker to emphasize each point with specified marker.

import matplotlib.pyplot as plt 
import numpy as np 

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o')
#plt.plot(ypoints, marker = '*')
plt.show()

# Format Strings "fmt" --