import os

r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"

W = f"{w}\033[1;47m"
R = f"{w}\033[1;41m"
G = f"{w}\033[1;42m"
Y = f"{w}\033[1;43m"
B = f"{w}\033[1;44m"

logo = f"""{y}
	_____________________                              _____________________
	`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
	    \      :          \          |:   |          /         :       /    
	     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
	      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
	      |     ;::         ;::         ;::         ;::         ;::  |       
	      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       
	      /     :           :           :           :           :    \       
	     /______::_____     ::    .     ::    .     ::   _____._::____\      
	                   `----._:: ::'  :   :: ::'  _.----'                    
	                          `--.       ;::  .--'                           
	                              `-. .:'  .-'                               
	                                 \    /                             
	                                  \  /                                   
	                                   \/

	                           {w} T.E.S.T L.O.G.O
"""
#print (logo)

def menu():
    os.system("clear")
    print(logo)
    print(f"""          {W}\033[2;30m Choisissez une option ou tapper exit pour sortir {w}

        {w}{y}  01{w} Information  {d} Information sur une personne.
        {w}{y}  02{w} Mailfinder   {d} Trouver une adresse e-mail.
        {w}{y}  03{w} Phoneinfo    {d} Information téléphone.
        {w}{y}  04{w} Véhicules    {d} Trouver un véhicule.
        {w}{y}  05{w} Casier       {d} Casier judiciaire.
        {w}{y}  06{w} IPlocation   {d} IP to location tracker.
        """)

if __name__ == "__main__":
    menu()
