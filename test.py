import sh
from sh import ifconfig
from sh import find
from sh import uname
# pip3 install sh

print(sh.ls("-l","/home/tuxstory",color="auto"))
print(ifconfig("wlp3s0"))
p = find("-name", "test.py", _bg=True)
print(p)
kernel = uname("-r")
print("Version du noyau Linux : ",kernel)
