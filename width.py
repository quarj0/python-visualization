from matplot import *

red = 'red'
blue = 'blue'
green = 'green'

lw1 = 2.5
lw2 = 2.8
lw3 = 3.5

dash = '--'
dot = ':'
sqw = 's'

plt.plot(x,x+1,color=red,lw=lw1,linestyle=dash,markersize=5)
plt.plot(x,x+2,color=blue,lw=lw2,linestyle=dot,markersize=5)
plt.plot(x,x+3,color=green,lw=lw3,markersize=5)
plt.plot(x,x+4,color='purple',marker="*",markersize=5)
plt.show()