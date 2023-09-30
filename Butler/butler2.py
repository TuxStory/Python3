import sqlite3

# Créer une connexion à la base de données
conn = sqlite3.connect("quiz.db")

# Créer un curseur pour la base de données
cur = conn.cursor()

# Créer la table des questions
cur.execute("CREATE TABLE questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, reponse1 TEXT, reponse2 TEXT, reponse3 TEXT, reponse4 TEXT, bonne_reponse INTEGER)")

# Insérer des questions dans la table
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quelle est la capitale de la France ?', 'Paris', 'Marseille', 'Lyon', 'Toulouse', 1)")
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quel est le nombre de planètes dans le système solaire ?', '8', '9', '10', '11', 1)")
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quel est le symbole chimique de l oxygene ?', 'O2', 'O', 'H2O', 'CO2', 1)")
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quelle est la capitale des États-Unis ?', 'Washington D.C.', 'New York', 'Los Angeles', 'Chicago', 1)")
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quel est le nom du président des États-Unis ?', 'Joe Biden', 'Donald Trump', 'Barack Obama', 'Bill Clinton', 1)")
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quel est le nom du joueur le plus titré de l histoire du football ?', 'Lionel Messi', 'Cristiano Ronaldo', 'Pelé', 'Diego Maradona', 1)")
cur.execute("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES ('Quel est le nom du fleuve le plus long du monde ?', 'Amazone', 'Nil', 'Yangtsé', 'Mississippi', 1)")

# Fermer le curseur
#cur.close()

# Fermer la connexion à la base de données
#conn.close()

# Initialiser le score
score = 0

# Afficher le titre du quiz
print("Quiz de choix multiple")

# Parcourir les questions
for i in range(1, 11):
    # Récupérer la question et les réponses
    cur = conn.cursor()
    cur.execute("SELECT question, reponse1, reponse2, reponse3, reponse4, bonne_reponse FROM questions WHERE id = ?", (i,))
    question, reponse1, reponse2, reponse3, reponse4, bonne_reponse = cur.fetchone()
    cur.close()

    # Afficher la question
    print("Question {} :".format(i))
    print(question)

    # Afficher les choix multiples sous forme de liste
    print("Voici les choix multiples :")
    print(reponse1, reponse2, reponse3, reponse4)

    # Demander la réponse
    bonne_reponse = input("Votre réponse : ")

    # Vérifier la réponse
    if bonne_reponse == reponse1:
        score += 1
        print("Réponse correcte") 
