import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 10, color="skyblue")
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
#plt.savefig("matplotlib_histagram.png")
plt.show()