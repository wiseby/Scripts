import time

prevTime = time.time()

counter = 1
while(True):
    if (time.time() - prevTime >= 1):
        print("{}seconds".format(counter))
        counter += 1
        prevTime = time.time()

    if (counter > 10):
        break

import subprocess

listDir = subprocess.run("ls")

print(listDir)