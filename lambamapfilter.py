import os

def TRI(Tab):
    return sorted(Tab)


def Info(Robot):
    print(Robot,": ", len(Robot), "lettre")


def main():
    os.system("clear")
    Robots = ["Wall-E", "Eve", "Nono", "Johnny5", "M-o", "R2D2", "C3PO", "Bumblebee"]
    Robots_tri = TRI(Robots)
    print(Robots_tri)
    Infos = list(map(Info, Robots_tri))
    big = list(filter(lambda x : len(x) > 5  ,Robots_tri))
    print("BIG :", big)
    #-----------------------------------------------------
    colours = [ "red", "green", "yellow", "blue" ]
    things = [ "house", "car", "tree" ]
    coloured_things = [ (x,y) for x in colours for y in things ]
    print(coloured_things)
  

if __name__=="__main__":
    main()

