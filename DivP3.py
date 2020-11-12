def div3(Nombre):
    Verif = 0
    for chiffre in range(len(Nombre)):
        print ("Le chiffre n°",chiffre,"est :",Nombre[chiffre])
        Verif = Verif + int(Nombre[chiffre])
        print ("Total =",Verif)
    if Verif % 3 == 0:
        print ("")
        print (Nombre,"est divisible par 3!")
        print ("Car la somme des chiffres est un multiple de 3.")
    else:
        print ("Pas de chance!")

def main():
    Nb = input("Entrer un nombre:")
    print (Nb,"est-il divisible par trois ?")
    div3(Nb)
    Nb = int(Nb)
    print ("--- ",(Nb/3),"---" )

if __name__=="__main__":
    main()
