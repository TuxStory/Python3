import os

def main():
    os.system("clear")
    addition(5,5)
    print("Test2".center(15,"*"))
    sandwich()

def print_decorator(function):
    def new_function(a, b): # Nouvelle fonction se comportant comme la fonction à décorer
        print('Addition des nombres {} et {}'.format(a, b))
        ret = function(a, b) # Appel de la fonction originale
        print('Retour: {}'.format(ret))
        return ret
    return new_function # Ne pas oublier de retourner notre nouvelle fonction

@print_decorator
def addition(a,b):
    print("Hello World")
    return a + b    

def pain(func): # l'argument est une fonction
    def wrapper():
        print ("</------\>")
        func()
        print ("<\______/>")
    return wrapper # wrapper est une fonction

def ingredients(func): # l'argument est une fonction
    def wrapper():
        print ("!tomate!")
        func()
        print ("~salade~")
    return wrapper # wrapper est une fonction

@pain
@ingredients
def sandwich(food="--steak--"):
    print (food)

if __name__=="__main__":
    main()