import time , os

os.system("clear")
txt = "Hello World ! \nThis is a test.\nHope,it will work.\nSee You Soon!"

for i in range(0,len(txt)):
	print(txt[i],end="", flush=True)
	time.sleep(0.1)

print ("")

my_string = 'Hello world ! This is a test.'
time.sleep(0.3)
for i in range(0,5):
	print (my_string,end="\r")
	for j in range(0,len(my_string)):
		my_string = my_string[1:] + my_string[:1]
		print (my_string,end="\r")
		time.sleep(0.2)

print ("")
