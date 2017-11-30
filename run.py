import subprocess
import time
import fileinput, sys
import os.path
statusCommand = 'git status'
addCommand = "git add ."
commitCommand = 'git commit -m "Added"'
pushCommand = "git push"
removeIndexLock = "sudo rm -rf ./.git/index.lock"
commitCounter = 0
commits = 0

while commitCounter < 100000:
    if commitCounter % 2 == 0:
        for line in fileinput.input(["test.txt"], inplace=True):
            line = line.replace("car", "truck")
            # sys.stdout is redirected to the file
            sys.stdout.write(line)
    else:
        for line in fileinput.input(["test.txt"], inplace=True):
            line = line.replace("truck", "car")
            # sys.stdout is redirected to the file
            sys.stdout.write(line)
    try:
        os.remove('./.git/index.lock')
    except OSError:
        print os.path.isfile('./.git/index.lock')
    process = subprocess.Popen(statusCommand.split(), stdout=subprocess.PIPE)
    process = subprocess.Popen(addCommand.split(), stdout=subprocess.PIPE)
    process = subprocess.Popen(commitCommand.split(), stdout=subprocess.PIPE)
    time.sleep(1)
    process = subprocess.Popen(pushCommand.split(), stdout=subprocess.PIPE)
    time.sleep(1)
    print "One more commit added to github! It's ", commits, " since we started"
    commits += 1
    commitCounter += 1
    time.sleep(60)
