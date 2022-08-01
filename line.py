import numpy as np
from matplot import * # from the previous file
# plt.plot(x,y)
# plt.show()

plt.plot(x,x+3, 'g--')
plt.plot(x,x+2, 'r-.')
plt.plot(x,x+1,'brown')
plt.legend() # you nedd to provide some else nothing will show
plt.show("")