# 15 sep 2023 challenge3 AE

import socket, re, codecs

def main():
    # Connexion à la socket
    host = "challenge01.root-me.org"
    port = 52021
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Réception du messsage
    text=str(s.recv(1024))
    print(text)

    # Trouver la chaîne de carractères
    chaîne_extraite = re.findall(r"'[^']+'", text)
    print("Chaîne en rot13: ",str(chaîne_extraite))
    chaîne_extraite=str(chaîne_extraite)
    print(type(chaîne_extraite))

    # Décoder la chaine en rot13
    Decode = codecs.decode(chaîne_extraite, "rot13")
    print("Chaîne décodée : ",Decode)
    print(type(Decode))

    # Envoi de la réponse
    message=(str(Decode)+"\n").encode("utf-8")
    print(message)
    s.send(message)

    # Réception de la réponse
    response = str(s.recv(1024), encoding="utf-8")
    print("La réponse est :", response)
    s.close()

if __name__ == "__main__":
    main()
