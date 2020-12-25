#!/usr/bin/env python3

# advent of code, day 6
# oerms

def getNextGroup(fileH):
    """read from file handler until next group is complete. return group as array of answers per person.
    NOTE: file needs empty line as last line"""
    group = ""
    while True:
        newline = fileH.readline()
        if newline == '': # raise exception when eof
            raise
        elif newline == "\n":
            break
        group += newline
    # create dictionary from list
    return (group.replace("\n"," ")).split()

findstr = 'abcdefghijklmnopqrstuvwxyz'
def countGroup(group):
    """count union of answers in group"""
    questions = [ 0 for i in range(len(findstr)) ]
    for member in group:
        for char in member:
            questions[findstr.find(char)] = 1
    return sum(questions)

def countGroup2(group):
    """count intersection of answers in group"""
    if len(group) == 1:
        return len(group[0])
    else:
        charsinall = 0
        for char in group[0]:
            isinallGroups = True
            for member in group:
                if char not in member:
                    isinallGroups=False
                    break
            if isinallGroups == True:
                charsinall += 1
    return charsinall

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
        except:
            # after last line
            infileH.close()
            break
    print("sum of counts:", countsum)
    print("sum of counts in all:", countallsum)

