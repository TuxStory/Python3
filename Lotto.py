# une autre methode plus simple : tirage = random.sample(lotto,7) 
# lotto = tableau / 7 nombre d'items

import random, os

def grille():
    lotto = []
    for i in range (1,47):
        lotto.append(i)
    return lotto

def tirage(lotto):
    for b in range(1,8):
        boule = (random.choice(lotto))
        lotto.remove(boule)
        if b == 7:
            print ("Tirage ",str(b),"."*2,"Le numero complementaire est le :",boule)
        else:
            print ("Tirage ",str(b),"."*25,"La boule :",boule)

def main():
    os.system("clear")
    print ("LOTTO".center(49,"="))
    Grille = grille()
    tirage(Grille)

if __name__=="__main__":
    main()
