#!/usr/bin/env python3

# advent of code, day 11
# oerms

import cmath

def navigateStep(coord, direction, step):
    """update coordinate and direction, as per the step instruction"""
    #action = step[0]
    #value = step[1:]
    if step[0]=='N':
        return coord + 1j*int(step[1:]), direction
    elif step[0]=='S':
        return coord - 1j*int(step[1:]), direction
    elif step[0]=='E':
        return coord + int(step[1:]), direction
    elif step[0]=='W':
        return coord - int(step[1:]), direction
    elif step[0]=='L':
        return coord, direction*cmath.rect(1, int(step[1:])*cmath.pi/180)
    elif step[0]=='R':
        return coord, direction*cmath.rect(1,-int(step[1:])*cmath.pi/180)
    elif step[0]=='F':
        return coord + direction*int(step[1:]), direction
    else:
        raise

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test12"
    filename = "input12"

    print('part 1: moving along...')
    # using complex numbers...
    coord = complex(0)
    direction = complex(1) # 1 == east, 1j == north, -1 == west, -1j == south
    print('coordinates:', coord)
    print('direction:', direction)

    with open(filename) as fileH:
        for line in fileH:
            print(line.strip())
            coord, direction = navigateStep(coord, direction, line.strip())
            print('coordinates:', coord)
            print('direction:', direction)

    print('final coordinates:',coord)
    print('final direction:', direction)
    print('final distance:', abs(coord.real) + abs(coord.imag))

