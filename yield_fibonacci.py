#Permet de travailler sur le nombre généré et non sur une liste
#Meilleurs performance et gestion de la mémoire. 

def fibonacci_generator():
    current, nxt = 0,1
    while True:
        current, nxt = nxt, nxt + current
        yield current

def main():
    for m in fibonacci_generator():
        print(m,end=', ')
    print()

if __name__=="__main__":
    main()
    
