import os

def main():
    os.system("clear")
    hello(10,7) #Devrais être décorer!

def deco(fonction):
    def new_hello(a,b):
        c = 3
        print("Hello i'm a decorator!")
        fonction(a,b)
        print("You're Welcome!")
        print("A & B & C", a, b, c)
        summ = a + b + c
        print("Total :", summ)
    return new_hello

@deco
def hello(a,b):
    print("Hello world")
    print("A & B :", a , b )
    return a , b

if __name__=="__main__":
    main()
