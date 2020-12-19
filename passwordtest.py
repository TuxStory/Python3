import getpass
import os
import hashlib

password = "476871b047a99c942a27a37aa60ec6b1833a515d92130e46fdece95325d01c561a5c59d8e3fbb0bc83dbf8ce5c9ccc244d4bc284072f6cecebb5dfa3e4859d63"

def verify():
    x = 0
    while x <= 2:
        mdp = hashlib.sha512()
        pswd = getpass.getpass('Password:')
        pswd = str(pswd).encode("utf-8")
        mdp.update(pswd)
        if mdp.hexdigest() == password:
            print("Welcome!")
            return True
        elif mdp.hexdigest() != password:
            print("Wrong password !")
            x = x + 1

os.system("clear")
print("*"*14)
print("* User Login *")
print("*"*14)
print("")

test = verify()
if test == True:
    print ("You are in!")
elif test != True:
    print ("Bye!")
    exit()
