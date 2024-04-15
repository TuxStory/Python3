import time
import cursor

cursor.hide()
print ('\033[? 25l', end="")

print ("\033[1;32m===================")
print ("   Terminal V2.5   ")
print ("===================\n")

Theme='⣾⣽⣻⢿⡿⣟⣯⣷'

for j in range(10):
   for i in Theme:
    print ("\033[1;32m >", i,"Processing ... ",end="\r")
    time.sleep(0.1)
