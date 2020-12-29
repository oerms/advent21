#!/usr/bin/env python3

# advent of code, day 11
# oerms

import numpy as np

def initializeSeats(filename):
    """load seats from filename"""
    seats = []
    with open(filename) as fileH:
        for line in fileH:
            seats.append([(0 if char=='L' else -1) for char in line])
    return np.array(seats)

def evolveSeats(seats,tempSeats):
    """evolve reactor grid pocket by one cycle"""
    for (i,j) in [(i,j) for i in range(len(seats)) for j in range(len(seats[0]))]:
        if not seats[i,j] == -1:
            numOccupiedNear = countNeighbors(seats,i,j)
            #if i<3 and j<2:
                #print(i,j)
                #print(numOccupiedNear)
            if seats[i,j] == 0 and numOccupiedNear == 0:
                tempSeats[i,j] = 1
            elif seats[i,j] == 1 and numOccupiedNear >= 4:
                tempSeats[i,j] = 0
            else:
                tempSeats[i,j] = seats[i,j]
    return tempSeats, seats

def countOccupiedSeats(seats):
    """count occupied seats of given array of seats"""
    return (seats == 1).sum()

def countNeighbors(seats,xcoord,ycoord):
    """count neighbors of coords in seat array"""
    count = 0
    for (x,y) in [(xcoord+i,ycoord+j) for i in range(-1,2) for j in range(-1,2)]:
        if x >= 0 and x < len(seats) and \
           y >= 0 and y < len(seats) and \
           seats[x,y] == 1:
            count += 1
    if seats[xcoord,ycoord]==1:
        count -= 1
    return count

if __name__ == "__main__":
    # change order of following for less steps or testcase
    filename = "test11"
    filename = "input11"

    print('part 1')
    seats = initializeSeats(filename)
    #print('initial state')

    cycle = 0
    tempSeats = seats.copy()
    occupiedSeats = countOccupiedSeats(seats)
    #print(seats)
    #print('occupied seats after cycle',cycle,':',occupiedSeats)
    oldOccupied = 0
    while True:
        oldOccupied = occupiedSeats
        seats, tempSeats = evolveSeats(seats,tempSeats)
        cycle += 1
        #print(seats)
        occupiedSeats = countOccupiedSeats(seats)
        #print('occupied seats after cycle',cycle,':',occupiedSeats)
        #print('occupied seats after last cycle',cycle-1,':',oldOccupied)
        if oldOccupied == occupiedSeats:
            print('no change with last cycle! occupied seats:',occupiedSeats)
            break
        #if cycle == 3 :
            #break

    exit()
    print('part 2: four dimensions')
    grid4 = initializeReactor4(filename,numCycles)
    #print('initial state')
    #printGrid4(grid4,int(len(grid4)/2),int(len(grid4)/2))

    for cycle in range(numCycles):
        grid4 = evolveGrid4(grid4)
        print('sum after cycle',cycle+1,':',grid4.sum())
        #printGrid4(grid4,int(len(grid4)/2),int(len(grid4)/2))

