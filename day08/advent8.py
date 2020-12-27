#!/usr/bin/env python3

# advent of code, day 7
# oerms

def loadProgram(filename):
    """load rules from filename"""
    with open(filename) as fileH:
        program = [ (line.split()[0], int(line.split()[1])) for line in fileH ]
        for line in fileH:
            program.append(l)
    return program

def runProgram(program):
    """run the program of the handheld console"""
    currentInstr = 0
    accumulator = 0
    visited = []
    while True:
        #print('now trying instruction',currentInstr,':',program[currentInstr])
        if currentInstr in visited:
            #print(currentInstr, 'has been visited! returning accumulator', accumulator)
            return accumulator
        visited.append(currentInstr)
        if program[currentInstr][0] == 'acc':
            accumulator += program[currentInstr][1]
            currentInstr += 1
        elif program[currentInstr][0] == 'jmp':
            currentInstr += program[currentInstr][1]
        else: #program[currentInstr][0] == 'nop':
            currentInstr += 1

if __name__ == "__main__":
    filename = "test8b"
    filename = "test8"
    filename = "input8"
    program = loadProgram(filename)
    # part 1
    accumulator = runProgram(program)
    print('accumulator at point where instruction would have been re-visited:', accumulator)


