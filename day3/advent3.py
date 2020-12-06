#!/usr/bin/env python3

# advent of code, day3
# oerms

def treesOnSlope(rowsDown, colsRight):
    """count trees on slope.
    input: int: rowsDown, int: colsRight
    return: number of trees on slope"""
    # result variable and column index
    numTrees = 0
    column = 0
    # file handler
    infileH = open("input3","r")
    while True:
        try:
            # read line, replace newline and test for tree and add
            newline = infileH.readline().replace('\n',"")
            if newline[column] == '#':
                numTrees += 1
            # increment column and skip lines
            column = (column + colsRight) % len(newline)
            for i in range(rowsDown-1):
                newline = infileH.readline().replace('\n',"")
        except:
            infileH.close()
            print("number of trees: ",numTrees)
            return numTrees

slopes = [
        [1,1],
        [1,3],
        [1,5],
        [1,7],
        [2,1]]

# result variable
treeProd = 1
for rowsDown,colsRight in slopes:
    print('down',rowsDown,'and right',colsRight)
    treeProd *= treesOnSlope(rowsDown, colsRight)
    print('product of trees:',treeProd)

