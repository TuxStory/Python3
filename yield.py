Names = ["John","Steve","Brian","Jim","Alex","Paul","Micheal","Bruce","Alfred","Buzz","Eric","Gary"]

Nombre = [i for i in range(1,1000000)]

def affiche(names):
    for name in names:
        yield name

def nextSquare():
    i = 1;
    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
                # from this point

def main():
    Test = affiche(Names)
    for nb in Test:
        print (nb)

    for nb in affiche(Nombre):
        print(nb)

    for num in nextSquare():
        if num > 100:
            break
        print(num)


if __name__=="__main__":
    main()

