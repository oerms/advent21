#!/usr/bin/env python3

# advent of code, day 4
# oerms

import re
import numpy as np

def validatePassport(batchDict, fields):
    """get a batch dictionary and validate for fields"""
    isValid = 1
    for field in fields:
        if field not in batchDict:
            isValid = 0
            break
    return isValid

def truelyValidatePassport(batchStr, fieldstests):
    """get a batch and validate for truely valid fields"""
    isValid = 1
    for field, testfunction in fieldstests:
        if field not in batchDict:
            isValid = 0
            break
        elif not testfunction(batchDict[field]):
            isValid = 0
            break
    return isValid

def getNextBatch(fileH):
    """read from file handler until next batch is complete. put into dictionary"""
    batch = ""
    while True:
        newline = fileH.readline()
        if newline == '': # raise exception when eof
            raise
        elif newline == "\n":
            break
        batch += newline
    # create dictionary from list
    batchList = (batch.replace("\n"," ")).split()
    batchDict = {}
    for pair in batchList:
        [key,val] = pair.split(':') 
        batchDict[key] = val
    return batchDict

rexpYr = re.compile('^[0-9]{4}$')
def byrTest(toTest):
    if rexpYr.match(toTest) == None:
        return False
    if int(toTest) < 1920 or int(toTest) > 2002:
        return False
    return True

def iyrTest(toTest):
    if rexpYr.match(toTest) == None:
        return False
    if int(toTest) < 2010 or int(toTest) > 2020:
        return False
    return True

def eyrTest(toTest):
    if rexpYr.match(toTest) == None:
        return False
    if int(toTest) < 2020 or int(toTest) > 2030:
        return False
    return True

rexpHgt = re.compile('^[0-9]{2,3}((cm)|(in))$')
def hgtTest(toTest):
    if rexpHgt.match(toTest) == None:
        return False
    if toTest[-2:] == 'cm':
        if int(toTest[:-2]) > 193 or int(toTest[:-2]) < 150:
            return False
    else:
        if int(toTest[:-2]) > 76 or int(toTest[:-2]) < 59:
            return False
    return True

rexpHcl = re.compile('^#[0-9A-Fa-f]{6}$')
def hclTest(toTest):
    if rexpHcl.match(toTest) == None:
        return False
    else:
        return True

rexpEcl = re.compile('^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))$')
def eclTest(toTest):
    if rexpEcl.match(toTest) == None:
        return False
    else:
        return True

rexpPid = re.compile('^[0-9]{9}$')
def pidTest(toTest):
    if rexpPid.match(toTest) == None:
        return False
    else:
        return True

# result variables and file handler
validPassports, truelyValidPassports = 0, 0
fields =       ['byr',   'iyr',   'eyr',   'hgt',   'hcl',   'ecl',   'pid']
testfunctions = [byrTest, iyrTest, eyrTest, hgtTest, hclTest, eclTest, pidTest]
infileH = open("input4","r")
while True:
    try:
        batchDict = getNextBatch(infileH)
        validPassports += validatePassport(batchDict, fields)
        truelyValidPassports += truelyValidatePassport(batchDict, np.transpose([fields, testfunctions]))
    except:
        # after last line
        infileH.close()
        print("valid passports:", validPassports)
        print("truely valid passports:", truelyValidPassports)
        break

