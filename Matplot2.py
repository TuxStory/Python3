import matplotlib.pyplot as plt
from numpy.random import normal,rand

x = normal(size=200)
plt.hist(x,bins=30)
plt.show()
