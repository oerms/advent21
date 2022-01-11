#!/usr/bin/env python3

# advent of code 2021, day 03
# oerms

import numpy as np

def loadData(filenme):
    """load data from filename"""
    with open(filename) as fileH:
        data = np.array([ list(line.strip()) for line in fileH ], int)
    return data

def findMostCommonBits(data):
    """check binary numbers in data for the most common bit on each place"""
    # position = [horizontal, depth]
    numPlaces = len(data[1])
    dataT = np.transpose(data)

    mostCommonBits = np.array([ sum(place) for place in dataT  ]) / len(dataT[0])

    return np.around(mostCommonBits).astype(int)

def findOxy(oxyData, place = 0):
    """find oxygen generator rating from oxyData:
        keep datums with most common bit at place (counting from zero)"""
    if len(oxyData) == 1:
        return oxyData[0]
    if place == len(oxyData[0]):
        raise

    #find most common bit
    ratio = sum(oxyData[:,place]) / len(oxyData)
    if ratio != 0.5:
        MCBatPlace = np.around(ratio).astype(int)
    else:
        MCBatPlace = 1

    #find datums to delete
    delSlice = [i for i in range(len(oxyData)) if oxyData[i,place] != MCBatPlace]

    oxyData = np.delete(oxyData, delSlice , 0)

    return findOxy(oxyData, place+1)

def findCO2(CO2Data, place = 0):
    """find CO2 scrubber rating from CO2Data:
        keep datums with least common bit at place (counting from zero)"""
    #print('')
    if len(CO2Data) == 1:
        return CO2Data[0]
    if place == len(CO2Data[0]):
        raise

    #find least common bit
    ratio = sum(CO2Data[:,place]) / len(CO2Data)
    if ratio != 0.5:
        MCBatPlace = np.around(ratio).astype(int)
    else:
        MCBatPlace = 1
    if MCBatPlace == 1:
        LCBatPlace = 0
    else:
        LCBatPlace = 1

    #find datums to delete
    delSlice = [i for i in range(len(CO2Data)) if CO2Data[i,place] != LCBatPlace]
    CO2Data = np.delete(CO2Data, delSlice , 0)

    return findCO2(CO2Data, place+1)


if __name__ == "__main__":
    # change order of following for testcase
    filename = "test03"
    filename = "input03"
    data = loadData(filename)

    print('part 1: find gamma rate')
    mostCommonBits = findMostCommonBits(data)
    MCBString = ''.join([str(place) for place in mostCommonBits])
    print('most common bits:', MCBString )
    print('gamme rate:', int(MCBString, 2) )
    invMCBString = ''.join([str(0) if char == '1' else str(1) for char in MCBString])
    print('epsilon rate:', int(invMCBString, 2) )
    print('power consumption:',int(MCBString, 2)*int(invMCBString, 2) )

    print('part 2: find life support rating')
    oxyData = np.copy(data)
    oxyRating = int(''.join([str(i) for i in findOxy(oxyData, 0)]), 2)
    print('oxigen generator rating:', oxyRating)
    CO2Data = np.copy(data)
    CO2Rating = int(''.join([str(i) for i in findCO2(CO2Data, 0)]), 2)
    print('CO2 scrubber rating:', CO2Rating)
    print('life support rating', oxyRating * CO2Rating)


