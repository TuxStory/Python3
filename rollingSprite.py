import time

sprite = ["\\","|","/","-"]
for i in range(1,50):
	for j in range(0,4):
		print (sprite[j],end="\r")
		time.sleep(0.1)
