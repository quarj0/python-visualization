import matplotlib.pyplot as plt
from seaborn import *
import seaborn as sns
import numpy as np


x = np.arange(0, 100,step=5)
y = x*x+2
fig ,axes = plt.subplots()

axes.set_ylabel("Y-label")
axes.set_xlabel("X-label")
axes.set_title("Sample Python Graph")

axes.plot(x, x**2, 'r*')
axes.plot(x, x**3,'g^')

axes.legend(["y=x**2", "y=x**3"],loc=2)
axes.grid(visible=True)
# axes.boxplot(x,y)
plt.show()