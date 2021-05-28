liste = {"Debian": 9,"Ubuntu":18.4,"Fedora":28,"Red Hat":9}

for dist,num in liste.items():
	print (dist.ljust(25,".") + str(num).rjust(5))

print (" ")
liste2 = ["Linux","FreeBSD","Unix","Windows","MacosX","BeOs"]

for o in liste2:
	print (o.ljust(25,"."))
