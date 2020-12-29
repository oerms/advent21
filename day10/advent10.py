#!/usr/bin/env python3

# advent of code, day 10
# oerms

import numpy as np

def loadAdapters(filename):
    """load adapter joltages from filename
    return sorted list of adapters, including outlet and final device"""
    adapters = np.loadtxt(filename,dtype=int)
    adapters = np.append(adapters,0)
    adapters = np.append(adapters,max(adapters)+3)
    adapters.sort()
    return adapters

def numCombinations(stretch):
    """number of combinations per stretch
    this function is not generic for all stretch lengths!"""
    if stretch == 1:
        # one difference of 1 is the only combination
        return 1
    elif stretch == 2:
        # two differences of 1 can either be kept or one adapter can be skipped
        return 2
    elif stretch == 3:
        # combinations for three '1's are the following 4: (1 1 1), (1 2), (2 1), (3)
        #   (here (1 2) means, that the second adapter has been skipped)
        return 4
    elif stretch == 4:
        # similar to == 3: seven combinations
        return 7
    else:
        print('stretch:',stretch)
        raise 

if __name__ == "__main__":
    # change order of lines for testcase
    filename = "test10a"
    filename = "test10b"
    filename = "input10"

    print('part 1')
    adapters = loadAdapters(filename)
    # get array of differences of joltages
    diffArray = np.diff(adapters)
    # count 1s and 3s
    diff1 = (diffArray == 1).sum()
    diff3 = (diffArray == 3).sum()
    print('Joltage differences of 1: diff1 =',diff1)
    print('Joltage differences of 3: diff3 =',diff3)
    print('diff1 * diff3:',diff1*diff3)

    print()
    print('part 2')
    # only stretches of consecutive joltage differences of '1' lead to new combinations
    #   because only then can you skip one or more adapters
    # get array indices where difference is 3 first, ...
    posOfThrees = np.where(diffArray == 3)[0]
    #   ... to then calculate the lengths of stretches of '1's
    stretches = np.diff(np.insert(posOfThrees,0,-1))-1 
    # to get the total number of combinations, the possible combinations coming from each stretch need to be multiplied
    totalCombinations = np.array([numCombinations(stretch) for stretch in stretches if stretch != 0]).prod()
    print('total combinations:',totalCombinations)

