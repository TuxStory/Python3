import matplotlib.pyplot as plt
import random, os

def carre():
    tab = []
    for y in range(-40, 44, 4):
        y = y*y
        tab.append(y)
    return tab
    
def cube():
    tab = []
    for y in range(-10, 11):
        y = y*y*y
        tab.append(y)
    return tab    
    
def puissance4():
    tab = []
    for y in range(-10, 11):
        y = y*y*y*y
        tab.append(y)
    return tab  

def main():
    x = list(range(-10,11))
    plt.title('Mathématique', color='green')
    y = carre()
    y3 = cube()
    #y4 = puissance4()
    plt.plot(x, y, label='Carre')
    plt.plot(x, y3, label='Cube')
    #plt.plot(x, y4, label='Puissance4')

    plt.ylabel("Y", color='red', fontweight='bold')
    plt.xlabel("X", color='red', fontweight='bold')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()