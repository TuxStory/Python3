import time
from tqdm import tqdm

bar = "#"
start_time = time.time()

for i in range(1,101):
	elapsed_time = time.time() - start_time
	print("Télechargement :",time.strftime("%M:%S",time.gmtime(elapsed_time)),"-",i,"% [",bar,end="\r")
	time.sleep(0.1)
	if i%10 == 0:
		bar=bar+("##")
print ("")

for i in tqdm(range(100)):
	time.sleep(0.1)
