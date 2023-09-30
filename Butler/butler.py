import sqlite3

# Ouvrir la base de données
conn = sqlite3.connect("quiz.db")

# Créer un curseur pour la base de données
cur = conn.cursor()

# Initialiser le score
score = 0

# Parcourir les questions
for i in range(1, 11):
    # Récupérer la question et les réponses
    cur.execute("SELECT question, reponse1, reponse2, reponse3, reponse4, bonne_reponse FROM questions WHERE id = ?", (i,))

    # Vérifier si le curseur renvoie None
    if cur.fetchone() is None:
        print("Il n'y a plus de questions.")
        break

    # Décompresser les résultats
    question, reponse1, reponse2, reponse3, reponse4, bonne_reponse = cur.fetchone()

    # Afficher la question
    print("Question {} :".format(i))
    print(question)

    # Afficher les choix multiples
    print("Voici les choix multiples :")
    print(reponse1, reponse2, reponse3, reponse4)

    # Demander la réponse
    bonne_reponse = input("Votre réponse : ")

    # Vérifier la réponse
    if bonne_reponse == reponse1:
        score += 1
        print("Réponse correcte !")
    else:
        print("Réponse incorrecte !")

# Afficher le score final
print("Votre score est de {}/10".format(score))

# Fermer le curseur
cur.close()

# Fermer la connexion à la base de données
conn.close()
