fichier = input("Entrez un fichier à ouvrir : ")
try:
	file = open(fichier,"a")
except IOError:
	file = open(fichier,"w")

print("\nContenu du fichier.")
print("-------------------")
print(" ")

with open(fichier) as f:
	read_data = f.read()
	print(read_data)
f.closed

while True:
	Message = input("Entrez du texte à ajouter : ")
	if Message.strip() == "quit":
		break
	file.write(Message + "\n" )
file.close()

