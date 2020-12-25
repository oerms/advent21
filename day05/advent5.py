#!/usr/bin/env python3

# advent of code, day 5
# oerms

def IDfromLine(line: str):
    """calculate seat ID from line input"""
    IDraw = line.replace('F','0')
    IDraw = IDraw.replace('B','1')
    IDraw = IDraw.replace('R','1')
    IDraw = IDraw.replace('L','0')
    return int(IDraw, 2)

def findmyID(IDlist):
    """find my seat from seatID list.
    the list holds both myID+1 and myID-1"""
    for myID in range(min(IDlist)+1,max(IDlist)-1):
        if myID+1 in IDlist and myID-1 in IDlist and myID not in IDlist:
            return myID

def readIDfile(filename: str):
    infileH = open(filename,"r")
    return [ IDfromLine(line.strip()) for line in infileH ]

if __name__ == "__main__":
    filename = "input5"
    IDlist = readIDfile(filename)
    print('maxID:', max(IDlist))
    print('minID:', min(IDlist))
    print('myID:',findmyID(IDlist))

