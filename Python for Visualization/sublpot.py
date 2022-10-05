import matplotlib.pylab as pb
import matplotlib.pyplot as plt
from seaborn import * 
import seaborn as sns
import numpy as np
import pandas as pd
import cv2 as cv


x=np.linspace(0,100,25)
y=x*x+2
pb.subplot(1,2,1)
pb.plot(x,y, 'r2')
pb.xlabel("X-axis")
pb.ylabel("Y-axis")
pb.title("SUBPLOT EXAMPLE", loc='center')
pb.subplot(1,2,2)
pb.plot(y,x, 'gP')
pb.ylabel("Y-axis")
pb.xlabel("X-axis")
pb.title("SUBPLOT EXAMPLE", loc='center')
pb.show()


