#!/usr/bin/env python3

# advent of code, day 11
# oerms

def loadSchedule(filename):
    """load earliest departure and bus schedule from file"""
    with open(filename) as fileH:
        earliest = int(fileH.readline().strip())
        #buslines = np.array([ int(no) for no in fileH.readline().strip().split(',') if no != 'x'])
        buslines = [ int(no) for no in fileH.readline().strip().split(',') if no != 'x']
        #buslines.sort()
    return earliest, buslines

def findBus(earliest, buslines):
    """given the earliest departure and the buslines in service, return the busline and the waiting time"""
    waitingTimes = [ ID - earliest%ID  for ID in buslines]
    waitingTime = min(waitingTimes)
    busline = buslines[waitingTimes.index(waitingTime)]
    return waitingTime, busline

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test13"
    filename = "input13"

    print('part 1: finding my bus...')
    earliest, buslines = loadSchedule(filename)
    print('earliest:',earliest)
    print('buslines:',buslines)
    waitingTime, busline = findBus(earliest, buslines)

    print('waiting time:', waitingTime)
    print('bus line:', busline)
    print('solution:', waitingTime*busline)

    exit()

    print('part 2: setting the waypoints...')
    # using complex numbers...
    coord = complex(0)
    waypoint = complex(10 + 1j) # 1 == east, 1j == north, -1 == west, -1j == south
    #print('coordinates:', coord)
    #print('direction:', waypoint)

    with open(filename) as fileH:
        for line in fileH:
            coord, waypoint = navigateByWaypoint(coord, waypoint, line.strip())
            #print('coordinates:', coord)
            #print('waypoint:', waypoint)

    print('final coordinates:',coord)
    print('final waypoint:', waypoint)
    print('final distance:', round(abs(coord.real) + abs(coord.imag)))

