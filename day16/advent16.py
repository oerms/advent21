#!/usr/bin/env python3

# advent of code, day 16
# oerms

import copy
from functools import reduce

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

        fileH.readline()
        myTicket = [int(i) for i in fileH.readline().strip().split(',')]

        fileH.readline()
        fileH.readline()
        while True:
            line = fileH.readline().strip()
            if line == '':
                break
            nearbyTickets.append([int(i) for i in line.split(',')])
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

def findFieldForValues(values, fields):
    """given the list of values, find the only valid field"""
    validFields = set( (field for field in fields) )
    for field in fields:
        # wenn alle values ins field passen, dann ist es valid, wenn nicht, entferne es vom set validFields
        for val in values:
            if (val < fields[field][0][0] or val > fields[field][0][1]) and \
               (val < fields[field][1][0] or val > fields[field][1][1]):
                validFields.remove(field)
                break
    if len(validFields) == 1:
        return validFields.pop()
    else:
        # return None, if there is more than one valid field
        return None

def findMyTicket(fields, myTicketValues, validTickets):
    """from the value ranges for each field, the values
    on my ticket and the valid tickets,
    find a dict of my fields and their values"""
    myTicket = {}
    # local copies for popping the items
    fieldsT = copy.copy(fields)
    myTicketValuesT = copy.copy(myTicketValues)
    validTicketsT = [list(i) for i in zip(*validTickets)] # transposed!

    # for the first position, there might be more than one valid field.
    #   so look for which position there might be only one valid field,
    #   put that field into myTicket and remove it and its position from all lists
    while len(fieldsT) > 0: 
        for pos, values in enumerate(validTicketsT):
            validField = findFieldForValues(values, fieldsT)
            # returns None if there is more than one valid field for the values.
            #   if there is only one valid field,
            #   add to myTicket and remove all data connected to it
            if validField != None:
                myTicket[validField] = myTicketValuesT[pos]
                fieldsT.pop(validField)
                myTicketValuesT.pop(pos)
                validTicketsT.pop(pos)
    return myTicket

if __name__ == "__main__":
    # change order of following lines to select testcase
    filename = "test16b"
    filename = "test16"
    filename = "input16"

    print('part 1: finding invalid values in nearby tickets...')
    fields, myTicketValues, nearbyTickets = loadTickets(filename)
    invalidValues, validTickets = findInvalidValues(nearbyTickets, fields)
    print('ticket scanning error rate (sum of invalid values):', sum(invalidValues))

    print('\npart 2: determining data for my ticket...')
    myTicket = findMyTicket(fields, myTicketValues, validTickets)
    print('Yay, found all the data for my ticket!')
    departValues = [ val for key, val in myTicket.items() if key[:4] in 'departure']
    departProd = reduce(lambda a,b: a*b, departValues)
    print('product of all "departure" field values:', departProd)

