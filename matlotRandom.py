import matplotlib.pyplot as plt
import random, os

def grille():
    tab = [random.randrange(1, 20) for i in range(10)]
    return tab

def main():
    x = [1,2,3,4,5,6,7,8,9,10]
    plt.title('Random Graph', color='green')
    line1 = grille()
    line2 = grille()
    line3 = grille()
#    line4 = grille()
#    line5 = grille()
    plt.plot( x, line1, label='Line1')
    plt.plot( x, line2, label='Line2')
    plt.plot( x, line3, label='Line3')
#    plt.plot( x, line4, label='Line4')
#    plt.plot( x, line5, label='Line5')

    plt.ylabel("Y", color='red', fontweight='bold')
    plt.xlabel("X", color='red', fontweight='bold')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()