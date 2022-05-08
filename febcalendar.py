import calendar

print ("="*20)
print ("Calendrier".center(20))
print ("="*20+"\n")

An = int(input("Quelle anneé : "))
Mois = int(input("Quel mois : "))
print ("\n"+calendar.month(An,Mois))
#print (calendar.calendar(An,Mois,0,6))

##Old
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(An,Mois)
print ("\n"+str+"\n")
print (c.pryear(An))
