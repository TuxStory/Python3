from bs4 import BeautifulSoup

PAGE = open("test.html","r")
soup = BeautifulSoup(PAGE, 'html.parser')

print ("TEST".center(30,"="))
print (soup.prettify())
print ("TEST2".center(30,"="))
print (soup.title)
print (soup.title.name)
print (soup.title.string)
print (soup.a)
print ("TEST3".center(30,"="))

for link in soup.find_all('a'):
    print(link.get('href'))

print ("TEST4".center(30,"="))

for link in soup.find_all('img'):
	print(link.get('src'))

print ("TEST5".center(30,"="))
#Twitter
for link in soup.find_all('div'):
	test = link.get('data-image-url')
	if test != None:
		print (test)
