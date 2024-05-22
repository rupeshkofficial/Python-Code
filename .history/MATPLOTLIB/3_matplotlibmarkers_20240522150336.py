# Marker Size - ms
# import matplotlib.pyplot as plt 
# import numpy as np 
# ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()


# Marker Edge Color - mec
# import matplotlib.pyplot as plt 
# import numpy as np 
# ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()



# Marker face color - mfc
# import matplotlib.pyplot as plt 
# import numpy as np 
# ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()

# Marker color both for edge and face
import matplotlib.pyplot as plt 
import numpy as np 
ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'y', mfc = 'r')
plt.show()