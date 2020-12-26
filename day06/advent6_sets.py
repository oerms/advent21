#!/usr/bin/env python3

# advent of code, day 6
# BONUS: with sets in python!
# oerms

from functools import *

def getNextGroup(fileH):
    """read from file handler until next group is complete. return group as array of sets of answers per person.
    NOTE: file needs empty line as last line"""
    group = []
    while True:
        newline = fileH.readline()
        if newline == '': # raise exception when eof
            raise ValueError
        elif newline == "\n":
            break
        group.append(set(newline.strip()))
    # create dictionary from list
    return group

def countGroup(group):
    """count union of answers in group"""
    #return len( reduce(lambda a,b: a.union(b), group) )
    return len( set.union(*group) )

def countGroup2(group):
    """count intersection of answers in group"""
    #return len( reduce(lambda a,b: a.intersection(b), group) )
    return len( set.intersection(*group) )

if __name__ == "__main__":
    #filename = "test6"  # uncomment for testfile
    filename = "input6"
    infileH = open(filename,"r")

    countsum = 0
    countallsum = 0
    while True:
        try:
            group = getNextGroup(infileH)
            countsum += countGroup(group)
            countallsum += countGroup2(group)
        except ValueError as exe:
            # after last line
            infileH.close()
            break
    print("sum of counts:", countsum)
    print("sum of counts in all:", countallsum)

