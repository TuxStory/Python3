import sqlite3

# Créer une connexion à la base de données
conn = sqlite3.connect("quiz.db")

# Créer un curseur pour la base de données
cur = conn.cursor()

# Créer la table des questions
cur.execute("CREATE TABLE questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, reponse1 TEXT, reponse2 TEXT, reponse3 TEXT, reponse4 TEXT, bonne_reponse INTEGER)")

# Insérer des questions dans la table
questions = [
    ("Quelle est la capitale de la France ?", "Paris", "Marseille", "Lyon", "Toulouse", 1),
    ("Quel est le nombre de planètes dans le système solaire ?", "8", "9", "10", "11", 1),
    ("Quel est le symbole chimique de l'oxygène ?", "O2", "O", "H2O", "CO2", 1),
    ("Quelle est la capitale des États-Unis ?", "Washington D.C.", "New York", "Los Angeles", "Chicago", 1),
    ("Quel est le nom du président des États-Unis ?", "Joe Biden", "Donald Trump", "Barack Obama", "Bill Clinton", 1),
    ("Quel est le nombre de joueurs dans une équipe de football ?", "11", "10", "9'", '8', 1),
    ("Quel est le nom du joueur le plus titré de l'histoire du football ?", "Lionel Messi", "Cristiano Ronaldo", "Pelé", "Diego Maradona", 1),
    ("Quel est le nom du fleuve le plus long du monde ?", "Amazone", "Nil", "Yangtsé", "Mississippi", 1),
]

# Insérer des questions dans la table
cur.executemany("INSERT INTO questions (question, reponse1, reponse2, reponse3, reponse4, bonne_reponse) VALUES (?, ?, ?, ?, ?, ?)", questions)

# Fermer le curseur
cur.close()

# Fermer la connexion à la base de données
conn.close()
