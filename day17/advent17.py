#!/usr/bin/env python3

# advent of code, day 17
# oerms

import copy
import numpy as np

def initializeReactor(filename,numCycles):
    """load rules from filename"""
    subgridInit = np.array(loadSubgridInput(filename))
    lensub = len(subgridInit)
    offset = numCycles+1
    lenGrid = 2*offset + lensub
    grid = np.zeros((lenGrid,lenGrid,lenGrid), dtype=int)
    #print(offset)
    #print(lenGrid)
    grid[offset:offset+lensub,offset:offset+lensub,int(len(grid)/2)] = subgridInit
    #print('reactor initialized')
    return grid

def loadSubgridInput(filename):
    """load input into array"""
    subgrid = []
    with open(filename) as fileH:
        for line in fileH:
            line = line.strip().replace('.','0').replace('#','1')
            subgrid.append([int(i) for i in line])
    #print('file loaded')
    return subgrid

def printGrid(grid,plane):
    """debugging: print a specific plane of the grid"""
    print('printing plane',plane)
    print(grid[:,:,plane])

def evolveGrid(grid):
    """evolve reactor grid pocket by one cycle"""
    tempGrid = grid.copy()
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            for k in range(1,len(grid)-1):
                numActiveNear = grid[i-1:i+2, j-1:j+2, k-1:k+2].sum()-grid[i,j,k]
                if numActiveNear in [2,3] and grid[i,j,k] == 1:
                    tempGrid[i,j,k]=1
                elif numActiveNear == 3 and grid[i,j,k] == 0:
                    tempGrid[i,j,k]=1
                else:
                    tempGrid[i,j,k]=0
    return tempGrid

""" PART 2 : FOUR DIMENSIONS """

def initializeReactor4(filename,numCycles):
    """load rules from filename"""
    subgridInit = np.array(loadSubgridInput(filename))
    lensub = len(subgridInit)
    offset = numCycles+1
    lenGrid = 2*offset + lensub
    grid = np.zeros((lenGrid,lenGrid,lenGrid,lenGrid), dtype=int)
    #print(offset)
    #print(lenGrid)
    grid[offset:offset+lensub,offset:offset+lensub,int(len(grid)/2),int(len(grid)/2)] = subgridInit
    #print('reactor initialized')
    return grid

def loadSubgridInput4(filename):
    """load input into array"""
    subgrid = []
    with open(filename) as fileH:
        for line in fileH:
            line = line.strip().replace('.','0').replace('#','1')
            subgrid.append([int(i) for i in line])
    #print('file loaded')
    return subgrid

def printGrid4(grid,planez,planew):
    """debugging: print a specific [planez,planew] of the grid"""
    print('printing plane',planez,planew)
    print(grid[:,:,planez,planew])

def evolveGrid4(grid):
    """evolve reactor grid pocket by one cycle"""
    tempGrid = grid.copy()
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            for k in range(1,len(grid)-1):
                for l in range(1,len(grid)-1):
                    numActiveNear = grid[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2].sum()-grid[i,j,k,l]
                    if numActiveNear in [2,3] and grid[i,j,k,l] == 1:
                        tempGrid[i,j,k,l]=1
                    elif numActiveNear == 3 and grid[i,j,k,l] == 0:
                        tempGrid[i,j,k,l]=1
                    else:
                        tempGrid[i,j,k,l]=0
    return tempGrid


if __name__ == "__main__":
    # change order of following for less steps or testcase
    filename = "test17"
    filename = "input17"
    numCycles = 2
    numCycles = 6

    print('part 1')
    grid = initializeReactor(filename,numCycles)
    #print('initial state')
    #printGrid(grid,int(len(grid)/2))

    for cycle in range(numCycles):
        grid = evolveGrid(grid)
        print('sum after cycle',cycle+1,':',grid.sum())
        #printGrid(grid,int(len(grid)/2)-1)
        #printGrid(grid,int(len(grid)/2))
        #printGrid(grid,int(len(grid)/2)+1)

    print('part 2')
    grid4 = initializeReactor4(filename,numCycles)
    #print('initial state')
    #printGrid4(grid4,int(len(grid4)/2),int(len(grid4)/2))

    for cycle in range(numCycles):
        grid4 = evolveGrid4(grid4)
        print('sum after cycle',cycle+1,':',grid4.sum())
        #printGrid4(grid4,int(len(grid4)/2),int(len(grid4)/2))

