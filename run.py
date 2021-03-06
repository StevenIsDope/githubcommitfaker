import subprocess
import time
import fileinput, sys
import os.path
import random

statusCommand = 'git status'
addCommand = "git add ."
commitCommand = 'git commit -m "Added"'
pushCommand = "git push"
removeIndexLock = "sudo rm -rf ./.git/index.lock"
commitCounter = 0

while commitCounter > -1:
    try:
        os.remove('./.git/index.lock')
    except OSError:
        print os.path.isfile('./.git/index.lock')
    timeToSleep = random.randint(1,43200)
    print "Going to sleep for ", timeToSleep, " seconds"
    for line in fileinput.input(["test.txt"], inplace=True):
        if "car" in line:
            line = line.replace("car", "truck")
            # sys.stdout is redirected to the file
            sys.stdout.write(line)
        elif "truck" in line:
            line = line.replace("truck", "car")
            # sys.stdout is redirected to the file
            sys.stdout.write(line)
    process = subprocess.Popen(statusCommand.split(), stdout=subprocess.PIPE)
    process = subprocess.Popen(addCommand.split(), stdout=subprocess.PIPE)
    process = subprocess.Popen(commitCommand.split(), stdout=subprocess.PIPE)
    time.sleep(1)
    process = subprocess.Popen(pushCommand.split(), stdout=subprocess.PIPE)
    time.sleep(1)
    print "One more commit added to github! It's ", commitCounter, " since we started"
    commitCounter += 1
    time.sleep(timeToSleep)
