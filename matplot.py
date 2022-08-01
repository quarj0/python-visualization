import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,25)
y=x*x+2
# plt.plot(x,y)
# plt.show()

plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.plot(y,x)
plt.show()
