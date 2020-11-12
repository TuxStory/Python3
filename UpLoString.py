import time
import cursor

# pip3 install cursor

cursor.hide()
Texte = "wavefx is processing ..."

for turn in range(1,5):
  for j in range(len(Texte)):
    print(end="\r")
    time.sleep(0.12)
    for i in range(len(Texte)):
      if  j == i:
        print(Texte[i].upper(),end="")
      else:
        print(Texte[i],end="")
print(" ")
