x = [[1,2,3],[3,4,5],[5,6,7]]
print(x)
import numpy as np
a = np.array(x)
print(a)


import matplotlib.pyplot as plt

%matplotlib inline 
x = np.linspace(0, 10, 100)
y = x ** 2

plt.plot(x,y
