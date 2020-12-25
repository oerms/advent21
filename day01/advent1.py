#!/usr/bin/env python3

# advent of code, day1
# oerms

# read input file into array
import numpy as np
inArray = np.loadtxt("input",dtype=int)

# find pair
try:
    for x in range(len(inArray)-1):
        for y in range(x):
            if inArray[x]+inArray[y] == 2020:
                print(inArray[x]*inArray[y])
                raise
except:
    pass

try:
    for x in range(len(inArray)-1):
        for y in range(x):
            for z in range(y):
                if inArray[x]+inArray[y]+inArray[z] == 2020:
                    print(inArray[x]*inArray[y]*inArray[z])
                    raise
except:
    pass

