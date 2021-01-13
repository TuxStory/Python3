import sh
from sh import ifconfig
from sh import find
# pip3 install sh

print(sh.ls("-l","/home/antoine",color="auto"))
print(ifconfig("wlp2s0"))
p = sh.find("-name", "test.py", _bg=True)
print(p)