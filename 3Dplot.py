from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax1=fig.add_subplot(1,1,1,projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,6,4,9,1,8,5,8,4,4]
#z=[7,4,0,2,5,6,3,9,7,1]
z2=[0,0,0,0,0,0,0,0,0,0]
dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x,y,z2,dx,dy,dz)


#ax1.plot_wireframe(x,y,z)
#ax1.scatter(x,y,z)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

#plt.show()

#ax1=fig.add_subplot(2,2,2,projection='3d')


plt.show()