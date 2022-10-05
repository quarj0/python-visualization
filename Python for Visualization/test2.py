import seaborn as sns
from matplotlib import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

# N = 8
# y = np.zeros(N)
# y1 = np.array([4,2,3])
# # pd.DataFrame(y1)
# x1 = np.linspace(0, 10, N, endpoint=True)
# x2 = np.linspace(0, 10, N, endpoint=False)
# plt.plot(x1, y, 'o')
# plt.plot(x2, y + 0.5, 'o')
# plt.draw_all(([-0.5, 1]))
# sns.boxplot(x2)
# sns.barplot(y1)
# # anim=mpla.Animation(x1,plt.gcf())
# # sns.clustermap(y1)
# plt.show()

# plot a subplot, of temperature, blood, and urine
# temperature range = 0,100
# blood , urine = 0,50
# print(np.arange(10,60,5))
fig, ax = 10
urine = 0, 10, 15, 20, 25, 30, 35, 40, 45, 50
# blood = np.sin(temp/5)
plt.title("test", loc='center')
fig =plt.subplots(1, 2 )
plt.show()