#!/usr/bin/env python3

# advent of code, day 16
# oerms

import copy

def loadTickets(filename):
    """load rules from filename"""
    fields = {}
    myTicket = []
    nearbyTickets = []
    with open(filename) as fileH:
        while True:
            line = fileH.readline().strip()
            if line == '':
                break
            field, valuesString = line.split(':')
            valueRanges = [ valuesString.split()[0], valuesString.split()[2] ]
            fields[field] = []
            for rnge in valueRanges:
                fields[field].append([ int(rnge.split('-')[0]), int(rnge.split('-')[1]) ]) 
        #print(fields)

        fileH.readline()
        myTicket = [int(i) for i in fileH.readline().strip().split(',')]
        #print(myTicket)

        fileH.readline()
        fileH.readline()
        while True:
            line = fileH.readline().strip()
            if line == '':
                break
            nearbyTickets.append([int(i) for i in line.split(',')])
        #print(nearbyTickets)
    return fields, myTicket, nearbyTickets

def findInvalidValues(nearbyTickets, fields):
    """taking the dict of fields, and the nearby tickets, return list of invalid fields"""
    invalidValues = []
    invalidTicketIndices = []

    for ticketIndex, ticket in enumerate(nearbyTickets):
        ticketIsValid = True
        for value in ticket:
            valueIsValid = False
            for key in fields:
                if (value >= fields[key][0][0] and value <= fields[key][0][1]) or \
                   (value >= fields[key][1][0] and value <= fields[key][1][1]):
                    valueIsValid = True
                    break
            if not valueIsValid:
                invalidValues.append(value)
                ticketIsValid = False
        if not ticketIsValid:
            invalidTicketIndices.append(ticketIndex)

    validTickets = [ ticket for ticketIndex, ticket in enumerate(nearbyTickets) if not ticketIndex in invalidTicketIndices ]

    return invalidValues, validTickets

if __name__ == "__main__":
    # change order of following for testcase
    filename = "input16"
    filename = "test16"
    filename = "test16b"

    fields, myTicket, nearbyTickets = loadTickets(filename)

    print('part 1: finding invalid values in nearby tickets...')
    invalidValues, validTickets = findInvalidValues(nearbyTickets, fields)
    print('ticket scanning error rate (sum of invalid values):', sum(invalidValues))

    print('part 2: determine fields...')
    print('valid tickets', validTickets)

