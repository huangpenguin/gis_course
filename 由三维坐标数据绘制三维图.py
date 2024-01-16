from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(70,131,1)
Y = np.arange(10,51,1)
X,Y = np.meshgrid(X,Y)
Z = [[0 for col in range(41)] for row in range(61)]
with open('C:\\Users\\lenovo\\Desktop\\assignment\\result') as f:
    for i in range(0,61):
        for j in range(0,41):
            line = f.readline()
            Z[i][j]=float(line.strip().split()[2])
Z=np.array(Z)
ax.plot_surface(X,Y,Z.T,rstride=1,cstride=1,cmap='rainbow')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude' )
ax.set_zlabel('Gravity anomalies (mgal)')
#ax.view_init(elev=0,azim=45)#旋转视角
plt.show()