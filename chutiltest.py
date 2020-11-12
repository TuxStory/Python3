import shutil 
import os

def main():
    os.chdir("/home/antoine/Bureau")
    shutil.copy("chutiltest.py","chutiltest-copie.py")
    print("Fichier copié      [ OK ]")
    os.unlink("chutiltest-copie.py")
    print("Fichier effacé     [ OK ]")
    
    #shutil.copytree('C:\\bacon', 'C:\\bacon_backup') Repertoire
    #shutil.move('C:\\bacon.txt', 'C:\\eggs') copie fichier -> dans rep
    #Calling os.unlink(path) will delete the file at path .
    #Calling os.rmdir(path) will delete the folder at path . This folder must be
    #empty of any files or folders.
    #Calling shutil.rmtree(path) will remove the folder at path , and all files
    #and folders it contains will also be deleted
    
    
if __name__=="__main__":
    main()