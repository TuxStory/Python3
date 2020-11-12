import numpy as np
import matplotlib.pyplot as plt
import random

listex=[]
listey=[]
listey2=[]
listex2=[]

for i in range(1,100):
	r=random.randint(0,100)
	r2=random.randint(0,100)
	listex.append(i)
	listex2.append(i)
	listey.append(r)
	listey2.append(r2)

x=listex
y=listey
x2=listex2
y2=listey2

plt.plot(x, y, label="1")
plt.plot(x2, y2, label="2")

plt.legend()
plt.show()
