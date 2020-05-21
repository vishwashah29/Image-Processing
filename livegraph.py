#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

#text="1,2 \n 2,9 \n 3,8 \n 4,2 \n 5,7 \n 6,3 \n 7,2 \n 8,5"
#saveFile=open('livegraphsample.txt','w')
#saveFile.write(text)
#saveFile.close()

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(x):
    graph_data=open('livegraphsample.txt','r').read()
    lines=graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)
    
ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()