#pip3 install progressbar2

import time
import progressbar

bar = progressbar.ProgressBar()
for i in bar(range(100)):
    time.sleep(0.02)

with progressbar.ProgressBar(max_value=10) as bar:
	for i in range(10):
		time.sleep(0.1)
		bar.update(i)

bar = progressbar.ProgressBar(redirect_stdout=True)
for i in range(100):
	print ('Some text', i)
	time.sleep(0.1)
	bar.update(i)

bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
for i in range(100):
	time.sleep(0.1)
	bar.update(i)

bar = progressbar.ProgressBar(widgets=[
	' [', progressbar.Timer(), '] ',
	progressbar.Bar(),
	' (', progressbar.ETA(), ') ',
])
for i in bar(range(20)):
	time.sleep(0.1)












