
import matplotlib.pyplot as plt
from seaborn import *
import numpy as np


x = np.linspace(0, 50, 25)
y = x*x+2
fig = plt.figure()
axes=fig.add_axes([0.1,0.5,0.5,0.5])
# axes.plot(x,y)
# 

fig, axes =plt.subplots(1,2)
for ax in axes:
    ax.plot(x,y,'orange')
plt.show()
