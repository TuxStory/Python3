import os

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#fonction trouvée sur internet
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def main():
    somme, size, size2 = 0,0,0
    dossier = input("Entrez un nom de dossier: ")
    for root, dirs, files in os.walk(dossier):
        print ("Dossier:",root.center(40,"-"))  
        total = 0
        for filename in files:
            name = bcolors.OKBLUE+filename+bcolors.ENDC
            size = bcolors.OKGREEN+sizeof_fmt(os.stat(root+"/"+filename).st_size)+bcolors.ENDC
            size2 = os.stat(root+"/"+filename).st_size
            print(name.ljust(50,".") + size)
            total = total + float(size2)
            somme = somme + float(size2)
        print("Total du dossier:",bcolors.HEADER+sizeof_fmt(total)+bcolors.ENDC,end="\n\n")
        somme = somme + float(size2)
    print("Total :",bcolors.WARNING+sizeof_fmt(somme)+bcolors.ENDC)
        
if __name__=="__main__":
    main()
            