from tqdm import *
import time, subprocess

mot = input("Entrez un mot :")
pbar = tqdm(total=100,ascii=True)
pbar.set_description("Analyse...")
for i in range(len(mot)):
    time.sleep(0.1)
    pbar.update(100/len(mot))
pbar.close()
