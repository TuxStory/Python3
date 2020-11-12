from itertools import product
from string import ascii_letters,digits
import time

charset = ascii_letters + digits

def pwd_checker(pwd):
    essai = 0
    start = time.time()
    time.clock()
    if 0 <len(pwd) <7:
        for i in range(1,7):
            for per in product(charset, repeat = i):
                essai = essai + 1
#                print ("Nombre d'essais :",essai,"longeur :",i,per,end="\r")
                if "".join(per) == pwd:
                    print ("")
                    print ("Le mot de passe est:", "".join(per))
                    print ("Nombre d'essais :", essai)
                    print (time.time() - start,"Secondes")
                    return
    else:
        print ("Password's length must be between 1 to 7")

def main():
    Mot = input("Entrer un mot de passe :")
    pwd_checker(Mot)

if __name__=="__main__":
    main()