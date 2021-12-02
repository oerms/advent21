#!/usr/bin/env python3

# advent of code 2021, day 01
# oerms

import numpy as np

def readfile(filename):
    """read file to get readings"""
    return np.loadtxt(filename,dtype=int)

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test01"
    filename = "input01"

    readings = readfile(filename)
    print(readings)

    print('part 1: sonar sweep')
    num_increases = sum([1 for i in range(len(readings)-1) if readings[i] < readings[i+1]])
    print(num_increases)

    print('part 2: sonar sweep - windowed')
    num_increases_window = sum([1 for i in range(len(readings)-3) if readings[i]+readings[i+1]+readings[i+2] < readings[i+1]+readings[i+2]+readings[i+3]])
    print(num_increases_window)

