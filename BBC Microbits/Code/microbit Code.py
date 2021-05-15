import microbit

while True:
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
        microbit.display.scroll("AB")
        break
    elif microbit.button_a.is_pressed():
        microbit.display.scroll("A")
    elif microbit.button_b.is_pressed():
        microbit.display.scroll("B")
    microbit.sleep(100)
 
 -----------------------------------------------------------------------------
 
import microbit

while True:
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
        microbit.display.scroll("AB")
        for i in range(5):
            for x in range(5):
                microbit.display.set_pixel(x,2,9)
                microbit.sleep(100)
                microbit.display.clear()
            for x in range(5):
                microbit.display.set_pixel(4-x,2,9)
                microbit.sleep(100)
                microbit.display.clear()    
        break
    elif microbit.button_a.is_pressed():
        microbit.display.scroll("A")
        microbit.display.clear()
        for y in range(5):
            for x in range(5):
                microbit.display.set_pixel(x,y,9)
                microbit.sleep(100)
                microbit.display.clear()
    elif microbit.button_b.is_pressed():
        microbit.display.scroll("B")
        for x in range(5):
            for y in range(5):
                microbit.display.set_pixel(x,y,9)
                microbit.sleep(100)
                microbit.display.clear()
    microbit.sleep(100)
    
-------------------------------------------------------------------------------
#Compas
# Ecrit ton programme ici ;-)
import microbit

microbit.display.show(microbit.Image.HAPPY)
microbit.sleep(200)
microbit.display.clear()
microbit.compass.calibrate()

while True:
    needle = ((15 - microbit.compass.heading()) // 30) % 12
    microbit.display.show(microbit.Image.ALL_CLOCKS[needle])

-------------------------------------------------------------------------------
import microbit
import random

microbit.display.scroll("MicroPython")
while True:
    if microbit.accelerometer.was_gesture("shake"):
        microbit.display.scroll(str(microbit.temperature())+"C")
    if microbit.button_a.is_pressed():
        microbit.display.scroll("A")
        microbit.display.show(str(random.randint(1, 6)))
        microbit.sleep(300)
        microbit.display.clear()
    if microbit.button_b.is_pressed():
        microbit.display.scroll("B")
        microbit.display.clear()
        for i in range(5):
            for x in range(5):
                microbit.display.set_pixel(x,0,9)
                microbit.sleep(200)
                microbit.display.clear()
                for y in range(5):
                    microbit.display.set_pixel(0,y,9)
                    microbit.sleep(200)
                    microbit.display.clear()

-------------------------------------------------------------------------------

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
-------------------------------------------------------------------------------

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
-------------------------------------------------------------------------------
#menu.py
# Add your Python code here. E.g.

from microbit import *

def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
    Carre = [carre,carre2,carre3,carre2]
    for i in range(5):
        display.show(Carre, delay=200)
    display.clear()
    
def carre2():
    for i in range(10):
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
        
def arrows():
    for i in range(5):
        display.show(Image.ALL_ARROWS,delay=100)
    display.clear()

def boutons():
    display.scroll("Test button")
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.scroll("AB")
            break
        elif button_a.is_pressed():
               display.scroll("A")
        elif button_b.is_pressed():
            display.scroll("B")
        sleep(100)

def K2000():
    display.scroll("K2000")
    for i in range(30):
            for x in range(1,5):
                display.set_pixel(x-1,2,5)
                display.set_pixel(x,2,9)
                sleep(100)
                display.clear()
            for x in range(1,4):
                display.set_pixel(4-x,2,9)
                display.set_pixel(4-x+1,2,5)
                sleep(100)
                display.clear()  

def main():
    display.scroll("A to select")
    while True:
        sleep(3000) 
        count = button_a.get_presses()
        display.scroll(str(count))

        #Shake
        if accelerometer.was_gesture("shake"):
            display.scroll("Pas si fort !")
        
        #count
        if count == 1:
            display.scroll(str(temperature())+"C")
        elif count == 2:
            carre()
        elif count == 3:
            carre2()
        elif count == 4:
            arrows()
        elif count == 5:
            boutons()
        elif count == 6:
            K2000()
        #remise à zero    
        count = 0

if __name__=="__main__":
    main()
-------------------------------------------------------------------------------
# Add your Python code here. E.g.

from microbit import *
import random

def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
    Carre = [carre,carre2,carre3,carre2]
    for i in range(5):
        display.show(Carre, delay=200)
    display.clear()
    
def carre2():
    for i in range(10):
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
        
def arrows():
    for i in range(5):
        display.show(Image.ALL_ARROWS,delay=100)
    display.clear()

def boutons():
    display.scroll("Test button")
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.scroll("AB")
            break
        elif button_a.is_pressed():
               display.scroll("A")
        elif button_b.is_pressed():
            display.scroll("B")
        sleep(100)

def K2000():
    display.scroll("K2000")
    for i in range(30):
            for x in range(1,5):
                display.set_pixel(x-1,2,5)
                display.set_pixel(x,2,9)
                sleep(100)
                display.clear()
            for x in range(1,4):
                display.set_pixel(4-x,2,9)
                display.set_pixel(4-x+1,2,5)
                sleep(100)
                display.clear()  

def boussole():
    compass.calibrate()
    while True:
        if compass.heading() >= 340 or compass.heading() <= 20:
            display.show("N")
        elif compass.heading() >= 70 and compass.heading() <= 100:
            display.show("E")
        elif compass.heading() >= 160 and compass.heading() <= 200:
            display.show("S")
        elif compass.heading() >= 250 and compass.heading() <= 290:
            display.show("O")  
        elif button_a.is_pressed():
            display.scroll("Bye")
            break    

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
    for i in range(10):
        display.show(Diamond, delay=200)
    display.clear()
    
        
def boulemagique():
    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
        ]

    while True:
        display.show('8')
        if accelerometer.was_gesture('shake'):
            display.clear()
            sleep(1000)
            display.scroll(random.choice(answers))
        sleep(10)
        if button_a.is_pressed():
            display.scroll("Bye")
            break
    
def main():
    display.scroll("A to select")
    while True:
        count = 0
        sleep(3000) 
        count = button_a.get_presses()
        display.scroll(str(count))

        #Shake
        if accelerometer.was_gesture("shake"):
            display.scroll("Pas si fort !")
        
        #count
        if count == 1:
            display.scroll(str(temperature())+"C")
        elif count == 2:
            carre()
        elif count == 3:
            carre2()
        elif count == 4:
            arrows()
        elif count == 5:
            boutons()
        elif count == 6:
            K2000()
        elif count == 7:
            boussole()
        elif count == 8:
            diamond()
        elif count == 9:
            boulemagique()
        #remise à zero    
        count = 0

if __name__=="__main__":
    main()
   ---------------------------------------------------------------------------
#Menu3.py
# Add your Python code here. E.g.

from microbit import *
import random

def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
    Carre = [carre,carre2,carre3,carre2]
    for i in range(5):
        display.show(Carre, delay=200)
    display.clear()
    
def carre2():
    for i in range(10):
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
        
def arrows():
    for i in range(5):
        display.show(Image.ALL_ARROWS,delay=100)
    display.clear()

def boutons():
    display.scroll("Test button")
    while True:
        if button_a.was_pressed() and button_b.is_pressed():
            display.scroll("AB")
            break
        elif button_a.is_pressed():
               display.scroll("A")
        elif button_b.is_pressed():
            display.scroll("B")
        sleep(100)

def K2000():
    display.scroll("K2000")
    for i in range(30):
            for x in range(1,5):
                display.set_pixel(x-1,2,5)
                display.set_pixel(x,2,9)
                sleep(100)
                display.clear()
            for x in range(1,4):
                display.set_pixel(4-x,2,9)
                display.set_pixel(4-x+1,2,5)
                sleep(100)
                display.clear()  

def boussole():
    compass.calibrate()
    while True:
        if compass.heading() >= 340 or compass.heading() <= 20:
            display.show("N")
        elif compass.heading() >= 70 and compass.heading() <= 100:
            display.show("E")
        elif compass.heading() >= 160 and compass.heading() <= 200:
            display.show("S")
        elif compass.heading() >= 250 and compass.heading() <= 290:
            display.show("O")  
        elif button_a.was_pressed():
            display.scroll("Bye")
            break    

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
    for i in range(10):
        display.show(Diamond, delay=200)
    display.clear()
    
        
def boulemagique():
    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
        ]

    while True:
        display.show('8')
        if accelerometer.was_gesture('shake'):
            display.clear()
            sleep(1000)
            display.scroll(random.choice(answers))
        sleep(10)
        if button_a.was_pressed():
            display.scroll("Bye")
            break
    
def compteur(count):
    #count
    if count == 1:
        display.scroll(str(temperature())+"C")
    elif count == 2:
        carre()
    elif count == 3:
        carre2()
    elif count == 4:
        arrows()
    elif count == 5:
        boutons()
    elif count == 6:
        K2000()
    elif count == 7:
        boussole()
    elif count == 8:
        diamond()
    elif count == 9:
        boulemagique()
    
def main():
    display.scroll("A to select")
    count=0
    while True:
        #sleep(3000) 
        if button_a.was_pressed():
            count = count + 1
        if button_b.is_pressed():
            display.clear()
            compteur(count)   
            count = 0
        if button_b.was_pressed():
            count = 0
        if count >= 10:
            display.scroll(str(count))
        else:
            display.show(str(count))
            
            
if __name__=="__main__":
    main()   
---------------------------------------------------------------------------
# Add your Python code here. E.g.

from microbit import *
import random, machine

def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
    Carre = [carre,carre2,carre3,carre2]
    for i in range(5):
        display.show(Carre, delay=200)
    display.clear()
    
def carre2():
    for i in range(10):
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
        
def arrows():
    for i in range(5):
        display.show(Image.ALL_ARROWS,delay=100)
    display.clear()

def boutons():
    display.scroll("Test button")
    while True:
        if button_a.was_pressed() and button_b.is_pressed():
            display.scroll("AB")
            break
        elif button_a.is_pressed():
               display.scroll("A")
        elif button_b.is_pressed():
            display.scroll("B")
        sleep(100)

def K2000():
    display.scroll("K2000")
    for i in range(30):
            for x in range(1,5):
                display.set_pixel(x-1,2,5)
                display.set_pixel(x,2,9)
                sleep(100)
                display.clear()
            for x in range(1,4):
                display.set_pixel(4-x,2,9)
                display.set_pixel(4-x+1,2,5)
                sleep(100)
                display.clear()  

def boussole():
    compass.calibrate()
    while True:
        if compass.heading() >= 340 or compass.heading() <= 20:
            display.show("N")
        elif compass.heading() >= 70 and compass.heading() <= 100:
            display.show("E")
        elif compass.heading() >= 160 and compass.heading() <= 200:
            display.show("S")
        elif compass.heading() >= 250 and compass.heading() <= 290:
            display.show("O")  
        elif button_a.was_pressed():
            display.scroll("Bye")
            break    

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
    for i in range(10):
        display.show(Diamond, delay=200)
    display.clear()
    
        
def boulemagique():
    answers = [
        "C'est certain",
        "Essaye encore",
        "Sans aucun doute",
        "Oui absolument",
        "C'est ton destin",
        "Le sort en est jeté",
        "D'après moi oui",
        "Outlook good",
        "Oui",
        "Peu probable",
        "Repose ta question",
        "Très probable",
        "Pas d'avis",
        "Essaye plus tard",
        "Tu peux compter dessus",
        "faut pas rêver",
        "C'est non",
        "Impossible",
        "Une chance sur deux",
        "C'est bien parti",
        ]

    while True:
        display.show('8')
        if accelerometer.was_gesture('shake'):
            display.clear()
            sleep(1000)
            display.scroll(random.choice(answers))
        sleep(10)
        if button_a.was_pressed():
            display.scroll("Bye")
            break

def face():
    while True:
        gesture = accelerometer.current_gesture()
        if gesture == "face up":
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
        if button_a.was_pressed():
            display.scroll("Bye")
            break    
        
def compteur(count):
    #count
    if count == 1:
        display.scroll(str(temperature())+"C")
    elif count == 2:
        carre()
    elif count == 3:
        carre2()
    elif count == 4:
        arrows()
    elif count == 5:
        boutons()
    elif count == 6:
        K2000()
    elif count == 7:
        boussole()
    elif count == 8:
        diamond()
    elif count == 9:
        boulemagique()
    elif count == 10:
        face()
    
def main():
    display.scroll("A to select")
    count=0
    while True:
        #sleep(3000) 
        if button_a.was_pressed():
            count = count + 1
        if button_b.is_pressed():
            display.clear()
            compteur(count)   
            count = 0
        if button_b.was_pressed():
            count = 0
        if count >= 10:
            display.scroll(str(count))
        else:
            display.show(str(count))
            
            
if __name__=="__main__":
    main()
----------------------------------------------------------------------------------
# Add your Python code here. E.g.

from microbit import *
import random

def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
    Carre = [carre,carre2,carre3,carre2]
    for i in range(5):
        display.show(Carre, delay=200)
    display.clear()
    
def carre2():
    for i in range(10):
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
        
def arrows():
    for i in range(5):
        display.show(Image.ALL_ARROWS,delay=100)
    display.clear()

def boutons():
    display.scroll("Test button")
    while True:
        if button_a.was_pressed() and button_b.is_pressed():
            display.scroll("AB")
            break
        elif button_a.is_pressed():
               display.scroll("A")
        elif button_b.is_pressed():
            display.scroll("B")
        sleep(100)

def K2000():
    display.scroll("K2000")
    for i in range(30):
            for x in range(1,5):
                display.set_pixel(x-1,2,5)
                display.set_pixel(x,2,9)
                sleep(100)
                display.clear()
            for x in range(1,4):
                display.set_pixel(4-x,2,9)
                display.set_pixel(4-x+1,2,5)
                sleep(100)
                display.clear()  

def boussole():
    compass.calibrate()
    while True:
        if compass.heading() >= 340 or compass.heading() <= 20:
            display.show("N")
        elif compass.heading() >= 70 and compass.heading() <= 100:
            display.show("E")
        elif compass.heading() >= 160 and compass.heading() <= 200:
            display.show("S")
        elif compass.heading() >= 250 and compass.heading() <= 290:
            display.show("O")  
        elif button_a.was_pressed():
            display.scroll("Bye")
            break    

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
    for i in range(10):
        display.show(Diamond, delay=200)
    display.clear()
    
        
def boulemagique():
    answers = [
        "C'est certain",
        "Essaye encore",
        "Sans aucun doute",
        "Oui absolument",
        "C'est ton destin",
        "Le sort en est jete",
        "D'après moi oui",
        "Outlook good",
        "Oui",
        "Peu probable",
        "Repose ta question",
        "Très probable",
        "Pas d'avis",
        "Essaye plus tard",
        "Tu peux compter dessus",
        "faut pas rever",
        "C'est non",
        "Impossible",
        "Une chance sur deux",
        "C'est bien parti",
        ]

    while True:
        display.show('8')
        if accelerometer.was_gesture('shake'):
            display.clear()
            sleep(1000)
            display.scroll(random.choice(answers))
        sleep(10)
        if button_a.was_pressed():
            display.scroll("Bye")
            break

def face():
    while True:
        gesture = accelerometer.current_gesture()
        if gesture == "face up":
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
        if button_a.was_pressed():
            display.scroll("Bye")
            break    

def time():
    t = running_time()
    display.scroll(str(round(t/60000))+" minutes")    
        
def compteur(count):
    #count
    if count == 1:
        display.scroll(str(temperature())+"C")
    elif count == 2:
        carre()
    elif count == 3:
        carre2()
    elif count == 4:
        arrows()
    elif count == 5:
        boutons()
    elif count == 6:
        K2000()
    elif count == 7:
        boussole()
    elif count == 8:
        diamond()
    elif count == 9:
        boulemagique()
    elif count == 10:
        face()
    elif count ==11:
        time()
    
def main():
    display.scroll("A to select")
    count=0
    while True:
        #sleep(3000) 
        if button_a.was_pressed():
            count = count + 1
        if button_b.is_pressed():
            display.clear()
            compteur(count)   
            count = 0
        if button_b.was_pressed():
            count = 0
        if count >= 10:
            display.scroll(str(count))
        else:
            display.show(str(count))
            
            
if __name__=="__main__":
    main()
    -------------------------------------------------------------
    while True:
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.show(str(random.randint(1, 6)))
    sleep(10)
    
    --------------------------------------------------------------------

