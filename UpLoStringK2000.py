import time 

Texte = "wavefx is processing"

for turn in range(1,6):
	for j in range(len(Texte)):
		print (end="\r")
		time.sleep(0.1)
		for i in range(len(Texte)):
			if  j == i:
				print(Texte[i].upper(),end="")
			else:
				print(Texte[i],end="")
		if turn%2 == 0:
			print (end="\r")
			for i in range(len(Texte)):
				if  j == len(Texte) - i:
					print(Texte[i].upper(),end="")
				else:
					print(Texte[i],end="")
print(" ")

