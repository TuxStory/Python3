from microbit import *

def bar(level):
    #intensity = 0
    for y in range(level):
        for i in range(10):
            for x in range(5):
                display.set_pixel(x,y,i)
                sleep(2)
    display.clear()


def main():
    number = [5,3,2,1,0,4,5,2,4,2,1,5]
    for level in number:
        bar(number[level])

main()