from tqdm import *
import time, subprocess

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.25)
    text = text + char

for i in trange(100):
    time.sleep(0.01)

for i in trange(100,ascii=True):
    time.sleep(0.01)

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.25)
    pbar.set_description("Processing %s" % char)

pbar = tqdm(total=100)
for i in range(100):
    time.sleep(0.1)
    pbar.update(1)
pbar.close()

for i in trange(10,ascii=True):
    ping = subprocess.run(["ping","-c 1","192.168.1.1"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(ping.stdout)
    #print(ping.stderr)
