import os

os.system("clear")
print ("="*24)
print ("Pourcentage".center(24," "))
print ("="*24)
print (" ")
total = 20
point = [17,18,16,12,14,11,9,19,7]
for i,p in enumerate(point):
	print ("Pourcentage ",i,": {:.2%}".format(point[i]/total))
