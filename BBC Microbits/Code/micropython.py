from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
                
carre = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999:")
              
carre2 = Image("00000:"
               "09090:"
               "09090:"
               "09990:"
               "00000:")

carre2 = Image("00000:"
               "09090:"
               "09090:"
               "09990:"
               "00000:")

carre3 = Image("00000:"
               "00000:"
               "00900:"
               "00000:"
               "00000:")
               
display.show(mystery)
sleep(100)
display.scroll("Carre")
for i in range(5):
    display.show(carre)
    sleep(100)
    display.show(carre2)
    sleep(100)
    display.show(carre3)
    sleep(100)

--------------------------------------------------------------------------------

from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()
    
def main():
    display.show(mystery)
    sleep(500)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed():
            carre()

main()
--------------------------------------------------------------------------------

from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()

def carre2():
    for x in range(5):
        display.set_pixel(x,0,9)
        sleep(200)
    for y in range(5):
        display.set_pixel(4,y,9)
        sleep(200)
    for x in range(5):
        display.set_pixel(4-x,4,9)
        sleep(200)
    for y in range(5):
        display.set_pixel(0,4-y,9)
        sleep(200)
    display.clear()

def main():
    display.show(mystery)
    sleep(300)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed():
            carre()
        if button_b.is_pressed():
            carre2()

main()
-------------------------------------------------------------------------------
from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()

def carre2():
    for i in range(5):
        for x in range(5):
            display.set_pixel(x,0,9)
            sleep(100)
        for y in range(5):
            display.set_pixel(x,y,9)
            sleep(100)
        for x in range(5):
            display.set_pixel(4-x,y,9)
            sleep(100)
        for y in range(5):
            display.set_pixel(0,4-y,9)
            sleep(100)
        display.clear()
        

def main():
    display.show(mystery)
    sleep(300)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed():
            carre()
        if button_b.is_pressed():
            carre2()

main()
--------------------------------------------------------------------------------

# Add your Python code here. E.g.
from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()

def carre2():
    for i in range(5):
        for x in range(5):
            display.set_pixel(x,0,9)
            sleep(100)
        for y in range(5):
            display.set_pixel(x,y,9)
            sleep(100)
        for x in range(5):
            display.set_pixel(4-x,y,9)
            sleep(100)
        for y in range(5):
            display.set_pixel(0,4-y,9)
            sleep(100)
        display.clear()
        
def diamond():
    diamond1 = Image("00100:01110:11111:01110:00100:")
    diamond2 = Image("00200:02220:22222:02220:00200:")
    diamond3 = Image("00300:03330:33333:03330:00300:")
    diamond4 = Image("00400:04440:44444:04440:00400:")
    diamond5 = Image("00500:05550:55555:05550:00500:")
    diamond6 = Image("00600:06660:66666:06660:00600:")
    diamond7 = Image("00700:07770:77777:07770:00700:")
    diamond8 = Image("00800:08880:88888:08880:00800:")
    diamond9 = Image("00900:09990:99999:09990:00900:")
    Diamond = [diamond1,diamond2,diamond3,diamond4,diamond5,diamond6,diamond7,diamond8,diamond9]
    for i in range(5):
        display.show(Diamond, delay=200)
    display.clear()
    
def main():
    display.show(mystery)
    sleep(300)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            diamond()
        elif button_a.is_pressed():
            carre()
        elif button_b.is_pressed():
            carre2()
        

main()
-----------------------------------------------------------------------
def info():
    ID = machine.unique_id()
    #name = '{:02x}{:02x}{:02x}{:02x}'.format(ID[0], ID[1], ID[2], ID[3])
    #ID = ID.decode('utf-8')
    freq = machine.freq()
    display.scroll("Frequence :")
    display.scroll(freq)
    display.scroll("ID :")
    display.scroll(ID)
    -------------------------------------------------------------------------
def acceleration():
    while True:
        if button_a.was_pressed():
            display.scroll("Bye")
            break
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        acceleration = math.sqrt(x**2 + y**2 + z**2)
        display.scroll(acceleration)
        sleep(500)
-------------------------------------------------------------------------------
 

