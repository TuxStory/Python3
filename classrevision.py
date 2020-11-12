class revi:
    i = 12345
    def message(self):
        return "Je suis une classe"

class Complex:
    def __init__(self, valeur1, valeur2):
        self.r = valeur1
        self.i = valeur2

class voiture:
    def __init__(self,HP,Année,model,couleur):
        self.HP = HP
        self.Année = Année
        self.model = model
        self.couleur = couleur
        self.roues = 4

    def affiche(self):
        print ("Je suis une voiture")
        print ("Une",self.model,"de couleur",self.couleur,"construite en",self.Année)
        print ("Chevaux =",self.HP)

x = revi()
print (x.i)
print (x.message())

x2 = Complex(6,3)
print (x2.r,x2.i)

skoda = voiture(120,2009,"Fabia","bleu")
skoda.affiche()
