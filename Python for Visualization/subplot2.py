import matplotlib.pyplot as plt
from seaborn import *
import seaborn as sns
import numpy as np


fig=plt.figure()
x = np.linspace(0, 50, 25)
y = x*x+2
axes1 = fig.add_axes([0.1,0.1,.8,.8])
axes2 = fig.add_axes([0.2, 0.5, .4, .34])
axes1.plot(x,y, 'bp')
axes2.plot(y,x,'gv')

# new graph

fig =plt.figure(figsize=(16,9), dpi=300)
fig.add_subplot()
plt.plot(x,y,'firebrick')
plt.show()
