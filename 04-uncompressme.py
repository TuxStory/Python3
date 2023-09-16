# 15 sep 2023 challenge4 AE
# NEED TO BE CORRECTED , AwFUL Code

import socket, re, base64 , zlib

def fonction(text):
    # Trouver la chaîne de carractères
    chaîne_extraite = re.findall(r"'[^']+'", text)
    print("Chaîne en base64 : ",str(chaîne_extraite))

    # Décoder la chaine en base64
    Decode = base64.b64decode(str(chaîne_extraite))
    print("Chaîne décodée : ",Decode)

    # Decode 2lib
    z = zlib.decompress(Decode)
    z = z.decode()
    print("zlib décompressé : ",z)

    # Envoi de la réponse
    message=(str(z)+"\n").encode("utf-8")
    print(message)
    return message

def main():
    # Connexion à la socket
    host = "challenge01.root-me.org"
    port = 52022
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Réception du message
    text=str(s.recv(1024))
    print(text)

    T1 = fonction(text)
    #print(type(T1))
    s.send(T1)
    # Réception de la réponse
    response = str(s.recv(1024), encoding="utf-8")
    print("La réponse est :", response)

    for i in ["T2","T3","T4"]:
        i = fonction(response)
        s.send(i)
        response = str(s.recv(1024), encoding="utf-8")
        print("La réponse est :", response)

    s.close()

if __name__ == "__main__":
    main()
