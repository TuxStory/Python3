import csv , os, random

def main():
    liste = []
    with open('question.csv') as csvfile:
        lecture = csv.reader(csvfile)
        for ligne in lecture:
            liste.append(ligne)
    hasard = random.randint(0,len(liste))
    #for i,question in enumerate(liste):
    print(liste[hasard][0])
    reponse = input("Votre réponse :")
    if reponse == liste[hasard][1]:
        print("Bravo!")
    else:
        print("Faux, ce n'est pas la bonne réponse!") 
            
if __name__=="__main__":
    os.system("clear")
    main()
