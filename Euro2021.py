def trier(Tab):
    Tri = dict(sorted(Tab.items(), key=lambda item: item[1], reverse=True))
    return Tri

def afficher(Tab):
    for Equipe,Score in Tab.items():
        print(Equipe," : ",Score)

def Tableau(Tab):
    Tab2=[]
    for Equipe in Tab:
        Tab2.append(Equipe[0])
    return Tab2

def main():

    #Groupe
    GA=["Italie","Suisse","Turquie","Pays de Galles"]
    GB=["Belgique","Danemark","Finlande","Russie"]
    GC=["Autriche","Pays-Bas","Ukraine","Macédoine du Nord"]
    GD=["Angleterre","Croatie","Rep. Tchèque","Ecosse"]
    GE=["Plogne","Espagne","Suède","Slovaquie"]
    GF=["France","Allemagne","Portugal","Hongrie"]

    #Score
    TabA={GA[0]:6,GA[1]:1,GA[2]:0,GA[3]:4}
    TabB={GB[0]:6,GB[1]:0,GB[2]:3,GB[3]:3}
    TabC={GC[0]:3,GC[1]:6,GC[2]:3,GC[3]:0}
    TabD={GD[0]:4,GD[1]:1,GD[2]:3,GD[3]:1}
    TabE={GE[0]:1,GE[1]:2,GE[2]:4,GE[3]:3}
    TabF={GF[0]:4,GF[1]:3,GF[2]:3,GF[3]:1}

    #Phase Finale
    TabFinal=[]

    #Affichage
    Tab_A = trier(TabA) ; afficher(Tab_A)
    print ("="*30)
    Tab_B = trier(TabB) ; afficher(Tab_B)
    print ("="*30)
    Tab_C = trier(TabC) ; afficher(Tab_C)
    print ("="*30)
    Tab_D = trier(TabD) ; afficher(Tab_D)
    print ("="*30)
    Tab_E = trier(TabE) ; afficher(Tab_E)
    print ("="*30)
    Tab_F = trier(TabF) ; afficher(Tab_F)

    #Selection
    TabFinal.extend((list(Tab_A.items())[0], list(Tab_A.items())[1]))
    TabFinal.extend((list(Tab_B.items())[0], list(Tab_B.items())[1]))
    TabFinal.extend((list(Tab_C.items())[0], list(Tab_C.items())[1]))
    TabFinal.extend((list(Tab_D.items())[0], list(Tab_D.items())[1]))
    TabFinal.extend((list(Tab_E.items())[0], list(Tab_E.items())[1]))
    TabFinal.extend((list(Tab_F.items())[0], list(Tab_F.items())[1]))

    #3eme
    TabFinal.append(list(Tab_A.items())[2])
    TabFinal.append(list(Tab_F.items())[2])
    print ()
    print (TabFinal)

    #Phase Finale
    PhaseFinale = Tableau(TabFinal)
    print (PhaseFinale)

if __name__=="__main__":
    main()

######################################################"
'''>>> dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

Test
    print (Tab_A.items())
    print (list(Tab_A.items())[0]
----------
contacts.items() returns pairs of key-value. In your case, that would be something like

(("John", 938477566), ("Jack", 938377264), ("Jill", 947662781))

Except that in python 3 this is like a generator and not a list. So you'd have to do list(contacts.items()) if you wanted to index it, which explains your error message. However, even if you did list(contacts.items())[0], as discussed above, you'd get the first pair of key-value.

What you're trying to do is fetch the value of a key if said key exists and contacts.get(key, value_if_key_doesnt_exist) does that for you.

contact = 'John'
# we use 0 for the default value because it's falsy,
# but you'd have to ensure that 0 wouldn't naturally occur in your values
# or any other falsy value, for that matter.
details = contacts.get(contact, 0)
if details:
    print('Contact details: {} {}'.format(contact, details))
else:
    print('Contact not found')
'''
