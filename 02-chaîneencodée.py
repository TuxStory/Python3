# 15 sep 2023 challenge2 AE

import socket, re, base64

def main():
    # Connexion à la socket
    host = "challenge01.root-me.org"
    port = 52023
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Réception des nombres
    text=str(s.recv(1024))

    # Trouver la chaîne de carractères
    chaîne_extraite = re.findall(r"'[^']+'", text)
    print("Chaîne en base64 : ",str(chaîne_extraite))

    # Décoder la chaine en base64
    Decode = base64.b64decode(str(chaîne_extraite))
    Decode = Decode.decode("utf-8")
    print("Chaîne décodée : ",Decode)

    # Envoi de la réponse
    message=(str(Decode)+"\n").encode("utf8")
    s.send(message)

    # Réception de la réponse
    response = str(s.recv(1024), encoding="utf-8")
    print("La réponse est :", response)
    s.close()

if __name__ == "__main__":
    main()
