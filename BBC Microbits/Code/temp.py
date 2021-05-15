from microbit import *

while True:
    temp = temperature()
    print((temp,))
    sleep(1000)