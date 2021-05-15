# Python-Volume-Meter.py
# Example Code for "Speech Recognition on a micro:bit" Article in micro:mag Issue 3
# Read P1 - Analog Volume Output Voltage from Microphone
# and Displays Voltage as a 15 LED Triangular Bargraph on micro:bit display

from microbit import *
import microbit

sample_delay = 50 # Sample Analog Voltage every 50 milliseconds


volume_min = 400 # Adjust this value until only 1 LEDs is illuminated when there is silence
volume_max = 750 # Adjust this value until all 15 LEDs are illuminated when the sound is loud
levels = 14
led_x = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
led_y = [4, 4, 3, 4, 3, 2, 4, 3, 2, 1, 4, 3, 2, 1, 0]


def bargraph(volume_level):  # Update Bargraph Display
    display.clear()
    for n in range(0, volume_level):
        display.set_pixel(led_x[n], led_y[n], 9)


while True:
    volume = pin1.read_analog()
#    print(volume)
    if volume < volume_min:
        volume = volume_min
    elif volume > volume_max:
        volume = volume_max
#    print(volume)
    volume_level = ((volume - volume_min)*levels)/(volume_max - volume_min)
    volume_level = (int(round(volume_level)) + 1)
#    print(volume_level)
    bargraph(volume_level)
    sleep(sample_delay)
