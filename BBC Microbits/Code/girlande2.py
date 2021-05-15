from microbit import *

while True:
    for y in range(5):
        for i in range(10):
            for x in range(5):
                display.set_pixel(x,y,i)
                sleep(10)