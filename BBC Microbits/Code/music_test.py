from microbit import *
import music

'''__name__        __init__        reset           set_tempo
get_tempo       play            pitch           stop
DADADADUM       ENTERTAINER     PRELUDE         ODE
NYAN            RINGTONE        FUNK            BLUES
BIRTHDAY        WEDDING         FUNERAL         PUNCHLINE
PYTHON          BADDY           CHASE           BA_DING
WAWAWAWAA       JUMP_UP         JUMP_DOWN       POWER_UP
POWER_DOWN'''

while True:
    if button_a.is_pressed():
        music.play(music.POWER_UP)
        display.scroll("UP")
    elif button_b.is_pressed():
        music.play(music.POWER_DOWN)
        display.scroll("DOWN")
