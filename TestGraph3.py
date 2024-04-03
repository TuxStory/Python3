import numpy as np
import matplotlib.pyplot as plt

listex=[] ; listey=[]
listex2=[] ; listey2=[]

#for i in range(10,100):
#	listex.append(i)
#	listey.append(i*i)
#	listex2.append(i)
#	listey2.append(i*i*i)

listex=[0,1, 3, 4, 6]
listey=[0,2, 3, 5, 12]
listex2=[0,1, 6, 9, 14]
listey2=[0,4, 7, 8, 13]

x=listex
y=listey
x2=listex2
y2=listey2

plt.plot(x, y, label="Test1")
plt.plot(x2, y2, label="Test2")

plt.legend()
plt.show()
