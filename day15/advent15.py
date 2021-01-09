#!/usr/bin/env python3

# advent of code, day 14
# oerms

import numpy as np

def playTheGameRecursive(numbers, length):
    """play the elves' number game using a recursive function. Quickly runs into the recursion limit of 1000..."""
    if len(numbers) >= length:
        return numbers
    else:
        if numbers[-1] not in numbers[:-1]:
            numbers = np.append(numbers, 0)
        else:
            whereLast = np.where(numbers == numbers[-1])[0]
            numbers = np.append(numbers, whereLast[-1] - whereLast[-2])
        return playTheGameRecursive(numbers, length)

def playTheGameLoop(numbers, length):
    """play the elves' number game using a while loop.
    This does not crash, but take much too long..."""
    print('current length:',len(numbers),end='')
    while len(numbers) < length:
        if numbers[-1] not in numbers[:-1]:
            numbers = np.append(numbers, 0)
        else:
            whereLast = np.where(numbers == numbers[-1])[0]
            numbers = np.append(numbers, whereLast[-1] - whereLast[-2])
        print('\rcurrent length:',len(numbers),end='',flush=True)
    print()
    return numbers

def playTheGameDict(numbers, stop):
    """play the elves' number game using a while loop and not keeping 
    all the numbers' positions, but only their last occurence.
    This still needs >10secs but ends in very finite time..."""
    nums = {}
    for i, num in enumerate(numbers):
        if num not in nums:
            nums[num] = [i]
        elif len(nums[num]) == 1:
            nums[num].append(i)
        else:
            nums[num] = [ nums[num][-1], i ]

    turn = len(numbers)
    lastSpoken = numbers[-1]

    while True:
        # print some progress
        if turn % 100000 == 0:
            print('\rcurrent turn:', turn+1 ,end='',flush=True)

        # find number to be spoken in current turn
        if nums[lastSpoken] == [ turn - 1 ]:
            thisSpoken = 0
        else:
            thisSpoken = nums[lastSpoken][-1] - nums[lastSpoken][-2]

        if turn == stop-1:
            print('\r', end='', flush=True)
            return thisSpoken

        # update dict entry
        if thisSpoken not in nums:
            nums[thisSpoken] = [turn]
        else:
            nums[thisSpoken] = [ nums[thisSpoken][-1], turn ]

        # prepare for next step
        lastSpoken = thisSpoken
        turn += 1

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test15b"
    filename = "test15c"
    filename = "test15d"
    filename = "test15e"
    filename = "test15"
    filename = "input15"

    with open(filename) as fileH:
        initNumbers = np.array(fileH.readline().strip().split(','), int)

    print('part 1: playing the elves\' number game')
    length = 2020
    #numbers = playTheGameLoop(initNumbers, length)    
    #print(length,'th number:', numbers[-1])
    lastNumber = playTheGameDict(initNumbers, length)    
    print(length,'th number:', lastNumber)

    print('part 2: count further!!')
    length = 30000000
    lastNumber = playTheGameDict(initNumbers, length)    
    print('30000000th number:', lastNumber)

