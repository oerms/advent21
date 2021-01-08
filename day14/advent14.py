#!/usr/bin/env python3

# advent of code, day 14
# oerms

""" common methods """

class WrongSize(Exception):
    """Exception class"""
    def __init__(self, length, mask, message="bitmask has wrong length!"):
        self.length  = length
        self.mask    = mask
        self.message = message

    def __str__(self):
        return self.message + ' ' + self.mask

def sumMemory(memory):
    """count the numbers in the memory"""
    numbers = [memory[address] for address in memory]
    return sum(numbers)

def decodeOperation(operation):
    """decode a line from the memory manupulation program file"""
    if operation[:3] == 'mas':
        mask = operation.split()[2]
        if len(mask) != 36:
            raise WrongSize(len(mask), mask)
        return 'mask', -1, mask
    if operation[:3] == 'mem':
        address = int(operation[ operation.find('[')+1 : operation.find(']') ])
        value = int(operation.split()[2])
        return 'mem', address, value 


""" PART 1: bitmasking values """

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
                next
            elif kind == 'mem':
                memory[address] = applyMask(value, mask)
    return memory


""" PART 2: version 2"""

def applyMasktoAddress(address, mask):
    """apply a mask with floating X to get a memory address with "floating" bits"""
    binAddress = format(address, '036b')
    if len(binAddress) != 36:
        raise WrongSize(len(binAdress), binAddress, message="Wrong length of address!")
    if len(mask) != 36:
        raise WrongSize(len(mask), mask, message="Wrong length of mask!")
    binAddressLst = list(binAddress)
    for pos in range(len(mask)):
        if mask[pos] == '0':
            next
        elif mask[pos] in ['1', 'X']:
            binAddressLst[pos] = mask[pos]
            next
    floatAddress = ''.join(binAddressLst)
    return floatAddress

def memAdrressFromFloating(floatAddress):
    """generator for the memory addresses according to the "bit mask" """
    if floatAddress.count('X') > 1:
        yield from memAdrressFromFloating(floatAddress.replace('X','1',1))
        yield from memAdrressFromFloating(floatAddress.replace('X','0',1))
    else:
        yield floatAddress.replace('X','1',1)
        yield floatAddress.replace('X','0',1)

def runInstructionsv2(filename):
    """run version 2 memory manipulations from filename"""
    memory = {}
    with open(filename) as fileH:
        for line in fileH:
            kind, address, value = decodeOperation(line.strip())
            if kind == 'mask':
                mask = value
                continue
            elif kind == 'mem':
                floatAddress = applyMasktoAddress(address, mask)
                for addr in memAdrressFromFloating(floatAddress):
                    memory[addr] = value
    return memory

if __name__ == "__main__":
    filename = "input14"

    print('part 1: initializing docking program...')
    #filename = "test14a"
    memory = runInstructionsfromFile(filename)
    sumofvalues = sumMemory(memory)
    print('final sum:', sumofvalues)

    print('part 2: version 2 of the chip with floating bits...')
    #filename = "test14b"
    memory = runInstructionsv2(filename)
    sumofvalues = sumMemory(memory)
    print('final sum:', sumofvalues)

