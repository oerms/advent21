#!/usr/bin/env python3

# advent of code, day 11
# oerms

import numpy as np
import math
from functools import reduce
import sys

def loadSchedule(filename):
    """load earliest departure and bus schedule from file"""
    with open(filename) as fileH:
        earliest = int(fileH.readline().strip())
        #buslines = np.array([ int(no) for no in fileH.readline().strip().split(',') if no != 'x'])
        buslines = [ int(no) for no in fileH.readline().strip().split(',') if no != 'x']
        #buslines.sort()
    return earliest, buslines

def findBus(earliest, buslines):
    """given the earliest departure and the buslines in service, return the busline and the waiting time"""
    waitingTimes = [ ID - earliest%ID  for ID in buslines ]
    waitingTime = min(waitingTimes)
    busline = buslines[waitingTimes.index(waitingTime)]
    return waitingTime, busline

def loadxSchedule(filename):
    """load bus lines and offsets for gold race from file"""
    with open(filename) as fileH:
        fileH.readline()
        schedule = [ item for item in fileH.readline().strip().split(',')]
        buslines = [ int(line) for line in schedule if line != 'x' ] 
        offsets = [ schedule.index(str(line)) for line in buslines ]
    return buslines, offsets

def findTimestamp(buslines, offsets):
    """find the timestamp from the bus IDs and the offsets
    this is the dumb brute force solution to part 2"""
    # sort bus lines from largest to smallest
    remainders = np.zeros(len(buslines))
    buses = [[i,j,k] for i,j,k in zip(buslines, offsets, remainders)]
    buses = sorted(buses, key=(lambda a: a[0]), reverse=True)
    busMultiplier = 1
    while True:
        timestamp = buses[0][0]*busMultiplier - buses[0][1]
        busMultiplier += 1
        for i in range(len(buses)):
            buses[i][2] = (timestamp + buses[i][1]) % buses[i][0]
        if all([buses[i][2] == 0 for i in range(len(buses))]):
            return timestamp
    return 

# the following two function definitions are from 
#  https://rosettacode.org/wiki/Chinese_remainder_theorem#Python or
#  https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
def chinese_remainder(n, a):
    """solver for chinese remainder system with n and a as inputs"""
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    """modulo inverse of a (mod b)"""
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def findsmartTimestamp(buslines, offsets):
    """find the timestamp from the bus IDs and the offsets
    this is the smarter approach to part 2"""
    # making the data for the solver of the chinese remainder problem
    # since the coefficients a would be negative, we have to look for the timestamp t+max(offsets)
    crtsystem = [buslines,[max(offsets)-offset for offset in offsets]]
    rem = chinese_remainder(*crtsystem)
    return rem - max(offsets) 

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test13"
    filename = "input13"

    print('part 1: finding my bus...')
    earliest, buslines = loadSchedule(filename)
    waitingTime, busline = findBus(earliest, buslines)
    print('waiting time:', waitingTime)
    print('bus line:', busline)
    print('solution:', waitingTime*busline)

    print('part 2: digging gold...')
    buslines, offsets = loadxSchedule(filename)
    # the following brute force approach does run fast enough
    #timestamp = findTimestamp(buslines, offsets)
    #print('timestamp:',timestamp)
    smarttimestamp = findsmartTimestamp(buslines, offsets)
    print('timestamp for first bus to start:', smarttimestamp)

