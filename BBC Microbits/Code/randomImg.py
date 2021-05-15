from microbit import *
import random

I = Image(5,5)
while True:
    I.set_pixel(random.randint(0,4),random.randint(0,4),random.randint(0,9))
    display.show(I)
    sleep(100)