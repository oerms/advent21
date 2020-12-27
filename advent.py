#!/usr/bin/env python3

# advent of code, day XXX
# oerms

import copy

class InfiniteLoop(Exception):
    """Exception class for infinite loops"""
    def __init__(self, position, message="Infinite loop detected"):
        self.position= position
        self.message = message

    def __str__(self):
        return self.message

def loadProgram(filename):
    """load rules from filename"""
    with open(filename) as fileH:
        program = [ [line.split()[0], int(line.split()[1])] for line in fileH ]
    return program

if __name__ == "__main__":
    filename = "test8b"
    filename = "test8"
    filename = "input8"
    program = loadProgram(filename)

    print('part 1')
    try:
        accumulator = runProgram(program)
        print(accumulator)
    except InfiniteLoop as err:
        print(err)
        print('recurring line:', err.position+1, '\naccumulator:', err.accumulator)
