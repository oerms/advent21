#!/usr/bin/env python3

# advent of code 2021, day 02
# oerms

def loadCommands(filenme):
    """load rules from filename"""
    with open(filename) as fileH:
        commands = [ [line.split()[0], int(line.split()[1])] for line in fileH ]
    return commands

def diveCommands(commands):
    """go from 0,0 by dive commands"""
    # position = [horizontal, depth]
    position = [0, 0]
    for command in commands:
        if command[0] == 'forward':
            position[0] += command[1]
        elif command[0] == 'down':
            position[1] += command[1]
        elif command[0] == 'up':
            position[1] -= command[1]
        else:
            print('wrong command:', command[0])
            exit()
        if position[1] < 0:
            print('negative depth:', position[1])
            exit()

    return position

def diveCommandsAim(commands):
    """go from 0,0 by dive commands"""
    # position = [horizontal, depth, aim]
    position = [0, 0, 0]
    for command in commands:
        if command[0] == 'forward':
            position[0] += command[1]
            position[1] += command[1] * position[2]
        elif command[0] == 'down':
            position[2] += command[1]
        elif command[0] == 'up':
            position[2] -= command[1]
        else:
            print('wrong command:', command[0])
            exit()
        if position[1] < 0:
            print('negative depth:', position[1])
            exit()

    return position


if __name__ == "__main__":
    # change order of following for testcase
    filename = "test02"
    filename = "input02"
    commands = loadCommands(filename)
    # print(commands)

    print('part 1: diving')
    finalPosition = diveCommands(commands)
    print('final position:', finalPosition )
    print('product of coordinates:', finalPosition[0] * finalPosition[1] )

    print('part 1: diving with aim')
    finalPositionAim = diveCommandsAim(commands)
    print('final position:', finalPositionAim )
    print('product of coordinates:', finalPositionAim[0] * finalPositionAim[1] )

