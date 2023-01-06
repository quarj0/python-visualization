import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

x = np.linspace(0,10,100)
fig  = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')