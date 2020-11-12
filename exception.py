import os
import subprocess

while True:
    try:
        x = int(input("Please enter a number: "))
        x/1
        #break
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
    except ZeroDivisionError as err:
        print (x,"N'est pas divisible par zéro.", err)
    else:
        print ("[OK]")
        break

nom=input("Entrer un mot:")
test= nom.isdigit()
if test == True:
    print ("Pas un mot!")

try:
    A = int(input("Entrer un nombre:"))
    B = int(input("Entrer un nombre:"))
    print (A/B)
except:
    print("Une erreur est survenue!")

try:
    C = input("Entrer un site web:")
    os.system("ping -c 4 "+C)
except OSError:
    print("une erreur est survenue! Le site existe t'il ?")
#ne fonctionne pas tel quel mais peut retourner 0 ou 1

try:
    C = input("Entrer un site web:")
    subprocess.call("ping -c 4 "+C,shell=True)
except OSError:
    print("une erreur est survenue! Le site existe t'il ?")

'''
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
'''

