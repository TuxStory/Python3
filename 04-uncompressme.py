# 15 sep 2023 challenge4 AE

import socket, re, base64 , zlib

def main():
    # Connexion à la socket
    host = "challenge01.root-me.org"
    port = 52022
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Réception du message
    text=str(s.recv(1024))
    print(text)

    # Trouver la chaîne de carractères
    chaîne_extraite = re.findall(r"'[^']+'", text)
    print("Chaîne en base64 : ",str(chaîne_extraite))

    # Décoder la chaine en base64
    Decode = base64.b64decode(str(chaîne_extraite))
    # Decode = Decode.decode("utf-8")
    print("Chaîne décodée : ",Decode)

    # Decode 2lib
    z = zlib.decompress(Decode)
    print(z)

    # Envoi de la réponse
    message=(str(z)+"\n").encode("utf-8")
    print(message)
    s.send(message)

    # Réception de la réponse
    response = str(s.recv(1024), encoding="utf-8")
    print("La réponse est :", response)
    s.close()

if __name__ == "__main__":
    main()
