import radio
import random
from microbit import *

radio.on()
while True:
    nouveau_message = str(radio.receive())
    if nouveau_message != "None":
        display.scroll(nouveau_message)
        display.clear()
