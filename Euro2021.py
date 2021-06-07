#Groupe
GA=["Italie","Suisse","Turquie","Pays de Galles"]
GB=["Belgique","Danemark","Finlande","Russie"]
GC=["Autriche","Pays-Bas","Ukraine","Macédoine du Nord"]
GD=["Angleterre","Croatie","Rep. Tchèque","Ecosse"]
GE=["Plogne","Espagne","Suède","Slovaquie"]
GF=["France","Allemagne","Portugal","Hongrie"]

#Score
TabA={GA[0]:0,GA[1]:0,GA[2]:0,GA[3]:0}
TabB={GB[0]:0,GB[1]:0,GB[2]:0,GB[3]:0}
TabC={GC[0]:0,GC[1]:0,GC[2]:0,GC[3]:0}
TabD={GD[0]:0,GD[1]:0,GD[2]:0,GD[3]:0}
TabE={GE[0]:0,GE[1]:0,GE[2]:0,GE[3]:0}
TabF={GF[0]:0,GF[1]:0,GF[2]:0,GF[3]:0}

#Phase Finale
TabFinale=[]

def affiche(Tab):
    for Equipe,Score in Tab.items():
        print(Equipe," : ",Score)

#Affichage
affiche(TabA)
print ("="*30)
affiche(TabB)
print ("="*30)
affiche(TabC)
print ("="*30)
affiche(TabD)
print ("="*30)
affiche(TabE)
print ("="*30)
affiche(TabF)

######################################################"
#>>> dict(sorted(x.items(), key=lambda item: item[1]))
#{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
