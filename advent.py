#!/usr/bin/env python3

# advent of code, day XXX
# oerms

# result variables
[validPWs, validPWsnew] = [0,0]

# file handler
infileH = open("input2","r")
while True:
    try:
        newline = infileH.readline()
    except:
        # after last line
        infileH.close()
        print("valid PWs old policy: ", validPWs)
        print("valid PWs new policy: ", validPWsnew)
        break

