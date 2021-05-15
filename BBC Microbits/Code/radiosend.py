import radio
import random
from microbit import *

radio.on()
while True:
    if button_a.was_pressed(): #is_pressed On appuie trop longtemps trop de message
        radio.send("Vous avez 1 Message!")
