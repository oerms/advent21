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

def evolveSeats(seats,tempSeats,rules="old"):
    """evolve seating area by one cycle"""
    for (i,j) in [(i,j) for i in range(len(seats)) for j in range(len(seats[0]))]:
        if not seats[i,j] == -1:
            if rules == "old":
                numOccupiedNear = countNeighbors(seats,i,j)
                if seats[i,j] == 0 and numOccupiedNear == 0:
                    tempSeats[i,j] = 1
                elif seats[i,j] == 1 and numOccupiedNear >= 4:
                    tempSeats[i,j] = 0
                else:
                    tempSeats[i,j] = seats[i,j]
            elif rules == "new":
                numOccupiedNear = countNeighbors(seats,i,j,countdepth=max(seats.shape))
                if seats[i,j] == 0 and numOccupiedNear == 0:
                    tempSeats[i,j] = 1
                elif seats[i,j] == 1 and numOccupiedNear >= 5:
                    tempSeats[i,j] = 0
                else:
                    tempSeats[i,j] = seats[i,j]
    return tempSeats, seats

def countOccupiedSeats(seats):
    """count occupied seats of given array of seats"""
    return (seats == 1).sum()

def countNeighbors(seats,xcoord,ycoord,countdepth=1):
    """count neighbors of coords in seat array"""
    count = 0
    # loop through directions
    for (i,j) in [(i,j) for i in range(-1,2) for j in range(-1,2)]:
        # move as deep as requested
        for depth in range(1,countdepth+1):
            x = xcoord + (i*depth)
            y = ycoord + (j*depth)
            # if within the seating area: do the counting
            if x >= 0 and x < len(seats) and y >= 0 and y < len(seats[0]):
                # if seat is taken, counter++ and go to next direction
                if seats[x,y] == 1:
                    count += 1
                    break
                # if seat is empty, no counter and go to next direction                 
                elif seats[x,y] == 0:
                    break
                # if there is no seat (== -1), go deeper
                else:
                    continue
            # if out of seating, go to next direction
            else:
                break
    if seats[xcoord,ycoord]==1:
        count -= 1
    return count

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test11"
    filename = "input11"

    print('part 1')
    seats = initializeSeats(filename)
    tempSeats = seats.copy()
    occupiedSeats = countOccupiedSeats(seats)
    cycle = 0
    oldOccupied = 0
    while True:
        oldOccupied = occupiedSeats
        seats, tempSeats = evolveSeats(seats,tempSeats)
        cycle += 1
        occupiedSeats = countOccupiedSeats(seats)
        #print('occupied seats after cycle',cycle,':',occupiedSeats)
        #print('occupied seats after last cycle',cycle-1,':',oldOccupied)
        if oldOccupied == occupiedSeats:
            print('no change with last cycle! occupied seats:',occupiedSeats, 'after',cycle-1,'cycles')
            break

    print('part 2: count along directions')
    seats = initializeSeats(filename)
    tempSeats = seats.copy()
    occupiedSeats = countOccupiedSeats(seats)
    cycle = 0
    oldOccupied = 0
    while True:
        oldOccupied = occupiedSeats
        seats, tempSeats = evolveSeats(seats,tempSeats,rules="new")
        cycle += 1
        occupiedSeats = countOccupiedSeats(seats)
        #print('occupied seats after cycle',cycle,':',occupiedSeats)
        #print('occupied seats after last cycle',cycle-1,':',oldOccupied)
        if oldOccupied == occupiedSeats:
            print('no change with last cycle! occupied seats:',occupiedSeats, 'after',cycle-1,'cycles')
            break
 
