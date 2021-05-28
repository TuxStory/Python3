# coding: utf-8

def generateur():
    yield "a"
    yield "b"
    yield "c"

i=generateur()
for v in i:
    print(v)

def generateur2(n):
    for i in range(n):
        if i == 5:
            print ("Quoi déjà 5eme tour?")
        yield i+1

i=generateur2(10)
for v in i:
     print(v)

#-------------------------------------------------
def fibonacci(n, a=0, b=1):
    for _ in range(n):
        yield a
        a, b = b, a + b

fi = fibonacci(10)
fi2 = fibonacci(5, 6, 7)
for num in fi:
    print(num)
for num in fi2:
    print(num)
#---------------------------------------------------

