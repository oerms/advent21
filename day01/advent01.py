#!/usr/bin/env python3

# advent of code 2021, day 01
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
        for line in fileH:
            coord, direction = navigateStep(coord, direction, line.strip())

    with open(filename) as fileH:
        program = [ [line.split()[0], int(line.split()[1])] for line in fileH ]
    return program

if __name__ == "__main__":
    # change order of following for testcase
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


    filename = "test12"
    filename = "input12"

    print('part 1: moving along...')
    # using complex numbers...
    coord = complex(0)
    direction = complex(1) # 1 == east, 1j == north, -1 == west, -1j == south

    with open(filename) as fileH:
        for line in fileH:
            coord, direction = navigateStep(coord, direction, line.strip())

    print('final coordinates:',coord)
    print('final direction:', direction)
    print('final distance:', round(abs(coord.real) + abs(coord.imag)))

    print('part 2: setting the waypoints...')
    # using complex numbers...
    coord = complex(0)
    waypoint = complex(10 + 1j) # 1 == east, 1j == north, -1 == west, -1j == south

