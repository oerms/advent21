#!/usr/bin/env python3

# advent of code, day 14
# oerms


class WrongSize(Exception):
    """Exception class"""
    def __init__(self, length, mask, message="bitmask has wrong length!"):
        self.length  = length
        self.mask    = mask
        self.message = message

    def __str__(self):
        return self.message + ' ' + self.mask

def decodeOperation(operation):
    """decode a line from the memory manupulation program file"""
    if operation[:3] == 'mas':
        mask = operation.split()[2]
        if len(mask) != 36:
            raise WrongSize(len(mask), mask)
        print(mask)
        return 'mask', -1, mask
    if operation[:3] == 'mem':
        address = int(operation[ operation.find('[')+1 : operation.find(']') ])
        value = int(operation.split()[2])
        print(address,value)
        return 'mem', address, value 

def applyMask(value, mask):
    """apply bit mask to value, return result"""
    # apply ones
    value = value | int( mask.replace('X','0'), 2)
    # apply zeros
    value = value & int( mask.replace('X','1'), 2)
    return value

def runInstructionsfromFile(filename):
    """run memory manipulations from filename"""
    memory = {}
    with open(filename) as fileH:
        for line in fileH:
            kind, address, value = decodeOperation(line.strip())
            if kind == 'mask':
                mask = value
                continue
            elif kind == 'mem':
                memory[address] = applyMask(value, mask)
    return memory

def sumMemory(memory):
    """count the numbers in the memory"""
    numbers = [memory[address] for address in memory]
    return sum(numbers)

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test14"
    filename = "input14"

    print('part 1: initializing docking program...')
    memory = runInstructionsfromFile(filename)
    sumofvalues = sumMemory(memory)
    print('final sum:', sumofvalues)
    exit()

    print('part 2: setting the waypoints...')
    # using complex numbers...
    coord = complex(0)
    waypoint = complex(10 + 1j) # 1 == east, 1j == north, -1 == west, -1j == south

