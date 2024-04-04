import os

def Affiche(itemsDict, leftWidth, rightWidth):
    print(' Users '.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

Users = {'User1' : 10, 'User2' : 25, 'User3' : 17, 'User4' : 84, 'User5' : 37 }

def Affiche2(Tab, Tab2, leftWidth, rightWidth):
    print(' Users '.center(leftWidth + rightWidth, '-'))
    for i in range(len(Tab)):
        print(Tab[i].ljust(leftWidth, '.') + str(Tab2[i]).rjust(rightWidth))

Tab = [ "User1", "User2", "User3", "User4", "User5"]
Tab2 = [ 10, 25, 17, 84, 37]

Tab3 = ["Debian", "Ubuntu", "Fedora", "OpenSuse", "Manjaro", "Red Hat"]
Tab4 = [12, 23.10, 39, 15.5, "rolling", 9.3]

os.system("clear")

Affiche(Users,20,3)
Affiche2(Tab,Tab2,20,3)
Affiche2(Tab3,Tab4,20,8)
