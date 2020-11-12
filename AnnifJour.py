from datetime import date
import calendar

jour = input("Le jour de votre naissance [1-31] :")
mois = input("Le mois de votre naissance [1-12] :")
an = input("Votre année de naissance [aaaa] :")

a,b,c = int(an),int(mois),int(jour)

now = date.today()
annif = date(a,b,c)
age = now - annif

print ("Vous êtes né(e) il y a",age.days,"jours.")
print ("Vous avez {0} ans.".format(int(age.days/365)))
print ("Le jour de votre naissance était un",calendar.day_name[annif.weekday()])
