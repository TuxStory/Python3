import os

for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)

print("test2".center(40,"="))

#-------------------------------
import subprocess

# define the ls command
ls = subprocess.Popen(["ls", "-p", "."],  
                      stdout=subprocess.PIPE,
                     )

# define the grep command
grep = subprocess.Popen(["grep", "-v", "/$"],  
                        stdin=ls.stdout,
                        stdout=subprocess.PIPE,
                        )

# read from the end of the pipe (stdout)
endOfPipe = grep.stdout

# output the files line by line
for line in endOfPipe:  
    print (line)

#--------------------------------
print("test3".center(40,"="))

import os, fnmatch

listOfFiles = os.listdir('.')  
pattern = "*.py"  
for entry in listOfFiles:  
    if fnmatch.fnmatch(entry, pattern):
            print (entry)
