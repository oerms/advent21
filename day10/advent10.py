#!/usr/bin/env python3

# advent of code, day 10
# oerms

import numpy as np

class DiffError(Exception):
    """Exception class for wrong difference in joltages"""
    def __init__(self, diff, message='wrong joltage difference!'):
        self.diff = diff
        self.message = message
    def __str__(self):
        return self.message


def loadAdapters(filename):
    """load adapter joltages from filename"""
    adapters = np.loadtxt(filename,dtype=int)
    adapters = np.append(adapters,0)
    adapters = np.append(adapters,max(adapters)+3)
    adapters.sort()
    return adapters

def findNumDifferences(adapters):
    """find number of differences: return [number of diff=1, num of diff=3]"""
    diff1 = 0
    diff3 = 0
    for adapter in range(len(adapters)-1):
        if adapters[adapter+1]-adapters[adapter] == 1:
            diff1 += 1
        elif adapters[adapter+1]-adapters[adapter] == 3:
            diff3 += 1
        else:
            raise DiffError(adapters[adapter+1]-adapters[adapter])
    return [diff1,diff3]

if __name__ == "__main__":
    # change order of lines for testcase
    filename = "test10a"
    filename = "test10b"
    filename = "input10"

    print('part 1')
    adapters = loadAdapters(filename)
    [diff1,diff3] = findNumDifferences(adapters)
    print('diff1:',diff1)
    print('diff3:',diff3)
    print('diff1 * diff3:',diff1*diff3)

