import time

A = "ILovePython"

for i in range(5):
    for i in range(len(A)):
        print (" "*i,A[i:i+1],end="\r")
        time.sleep(0.2)
        print (" "*(i*2),end="\r")
