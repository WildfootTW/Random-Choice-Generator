import random
import sys
import time

name = []

for line in sys.stdin:
#    print( line , end="")
    if line == "\n":
        print(name[ random.randrange(len(name)) ])
        del name[:]

    else:
        name.append(line)
        
print(time.strftime("%H:%M:%S"))
