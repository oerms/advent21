#!/usr/bin/env python3

# advent of code, day 7
# oerms

import copy

class InfiniteLoop(Exception):
    """Exception class for infinite loops"""
    def __init__(self, position, accumulator, message="Infinite loop detected"):
        self.position= position
        self.accumulator = accumulator
        self.message = message

    def __str__(self):
        return self.message

def loadProgram(filename):
    """load rules from filename"""
    with open(filename) as fileH:
        program = [ [line.split()[0], int(line.split()[1])] for line in fileH ]
    return program

def runProgram(program):
    """run the program of the handheld console"""
    position = 0
    accumulator = 0
    visited = []
    while True:
        if position in visited:
            raise InfiniteLoop(position, accumulator)
        if position == len(program):
            return accumulator
        visited.append(position )
        if program[position ][0] == 'acc':
            accumulator += program[position ][1]
            position += 1
        elif program[position ][0] == 'jmp':
            position += program[position ][1]
        else: #program[position ][0] == 'nop':
            position += 1

def fixProgram(program):
    """fixing given program my changing 'nop' to 'jmp' or vice versa
    arguments:
        list of tuples: program    
    return:
        int: position of change
        str: type of change
        int: accumulator"""
    try:
        return [-1, "no change", runProgram(program)]
    except InfiniteLoop as err:
        pass
    for position in range(len(program)):
        if program[position][0] == 'jmp':
            program[position][0] = 'nop'
            try:
                return [position, "'jmp' to 'nop'", runProgram(program)]
            except InfiniteLoop as err:
                program[position][0] = 'jmp'
                next
        elif program[position][0] == 'nop':
            program[position][0] = 'jmp'
            try:
                return [position, "'nop' to 'jmp'", runProgram(program)]
            except InfiniteLoop as err:
                program[position][0] = 'nop'
                next
        else:
            next
    raise Exception('no fix found!')


if __name__ == "__main__":
    filename = "test8b"
    filename = "test8"
    filename = "input8"
    program = loadProgram(filename)
    #for instruction in range(len(program)):
        #print(program[instruction])

    print('part 1')
    try:
        accumulator = runProgram(program)
        print(accumulator)
    except InfiniteLoop as err:
        print(err)
        print('recurring line:', err.position+1, '\naccumulator:', err.accumulator)

    print('\npart 2')
    [position,replacement,accumulator] = fixProgram(program)
    print('fix found on line',position+1,'replacement:',replacement,'accumulator:',accumulator)
