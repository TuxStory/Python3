# 15 sep 2023 challenge01 AE

import socket
import math
import re

def main():
    # Connexion à la socket
    host = "challenge01.root-me.org"
    port = 52002
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Réception des nombres
    text=str(s.recv(1024))

    # Le motif qui correspond aux deux nombres
    regex = r"\d+"

    # Utilisation de la fonction re.split() pour isoler les deux nombres
    numbers = re.findall(regex, text)

    # Affichage des deux nombres
    n1 = int(numbers[1])
    n2 = int(numbers[2])
    print("Nombre : ",n1,"+ ",n2)

    # Calcul de la racine carrée du premier nombre
    x = math.sqrt(n1)
    print("x le carré de n1 = ",x)

    # Calcul du produit
    y = x * n2
    print("y le produit de x * n2 = ",y)

    # Arrondissement du résultat
    z = round(y, 2)
    print(z)

    # Envoi de la réponse
    message=(str(z)+"\n").encode("utf-8")
    s.send(message)

    # Réception de la réponse
    response = str(s.recv(1024), encoding="utf-8")
    print("La réponse est :", response)
    s.close()

if __name__ == "__main__":
    main()
