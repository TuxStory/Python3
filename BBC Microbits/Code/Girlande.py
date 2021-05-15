from microbit import *

while True:
    for i in range(10):
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,i)
                sleep(10)
