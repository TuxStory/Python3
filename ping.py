import os

def ping(plage):
    for ip in range(255):
        test = os.system("ping -c 1 " +plage+str(ip)+" >/dev/null")
        if test == 0:
            print(plage+str(ip),"est actif sur le reseau.")

def main():
    os.system("clear")
    print("PingPy".center(25,"-"))
    print("\nExemple : 192.168.1.")
    print("Exemple : 192.168.0.")
    print("-"*25)
    Plage = input("Adresses reseau a scanner: ")
    ping(Plage)

if __name__=="__main__":
    main()
