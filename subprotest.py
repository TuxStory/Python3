import subprocess

subprocess.call("clear")
print ("ls".center(50,"-"))
subprocess.call("ls")
print ("ls 2".center(50,"-"))
subprocess.call(["ls", "-al"])
print ("ls 2".center(50,"-"))
subprocess.call(["uname", "-a"])


try:
    print ("ping".center(50,"-"))
    C = input("Entrer un site web:")
    subprocess.call("ping -c 4 "+C,shell=True)
except OSError:
    print("une erreur est survenue! Le site existe t'il ?")

try:
    print ("Test".center(50,"-"))
    subprocess.call("dfd")
except OSError:
    print("La commande n'existe pas !")

print ("Test".center(50,"-"))
a = subprocess.check_call("ls", shell=True)
print (a)
b = subprocess.check_output("ls", shell=True)
print (b)

#status = subprocess.call('ls -ls', stdout = myFh, shell = True)
print ("subprocess.check".center(50,"-"))
try:
    subprocess.check_call('ls -lsz', shell = True)
except subprocess.CalledProcessError as e:
    print (e.returncode)
    print (e.cmd)
    print (e.output)
