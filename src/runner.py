import os

files = [f for f in os.listdir() if ".py" in f and not "runner.py" in f]

for script in files:
    exec(open(script).read())
