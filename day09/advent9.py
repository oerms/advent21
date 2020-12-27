#!/usr/bin/env python3

# advent of code, day 09
# oerms

import copy
import numpy as np

class NoPairs(Exception):
    """Exception class for wrong XMAS encoding (no two numbers for next number)"""
    def __init__(self, position, nextNumber, message="no two numbers sum to next number"):
        self.nextNumber = nextNumber
        self.position   = position 
        self.message    = message
    def __str__(self):
        return self.message

class FoundPair(Exception):
    """Exception class for aborting search"""
    def __init__(self, message="pair found"):
        self.message = message
    def __str__(self):
        return self.message

def loadStream(filename):
    """load XMAS number stream from filename"""
    return np.loadtxt(filename,dtype=int)

def testXMASstream(stream,preLen):
    """test XMAS number stream"""
    for position in range(preLen,len(stream)-1):
        try:
            for i in range(position-preLen,position-1):
                for j in range(i+1,position):
                    if stream[i]+stream[j] == stream[position]:
                        raise FoundPair
        except FoundPair as err:
            next
        else:
            raise NoPairs(position, stream[position])
    return True

def findWeakness(stream,wrongPos):
    """find the encryption weakness in the stream, where number at wrongPos does not have pair"""
    for i in range(len(stream)-1):
        for j in range(i,0,-1):
            contRange = stream[j:i]
            if contRange.sum() == stream[wrongPos]:
                return min(contRange)+max(contRange)
            if contRange.sum() > stream[wrongPos]:
                break

if __name__ == "__main__":
    # change order of lines for testcase
    filename = "test9"
    filename = "input9"
    preLen = 5
    preLen = 25

    print('part 1')
    stream = loadStream(filename)
    try:
        testOK = testXMASstream(stream,preLen)
        print('stream OK?',testOK)
    except NoPairs as err:
        print('fail at position:', err.position, '\nnext number:', err.nextNumber)
        print('attempting to find weakness')
        weakness = findWeakness(stream,err.position)
        print('found weakness:',weakness)

