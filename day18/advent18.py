#!/usr/bin/env python3

# advent of code, day 18
# oerms

from functools import reduce

class InvalidTerm(Exception):
    """Exception class for invalid terms"""
    def __init__(self, term, message="Invalid Term"):
        self.term= term
        self.message = message
    def __str__(self):
        return self.message

def loadTerms(filename):
    """load math expressions from filename"""
    with open(filename) as fileH:
        terms = [ line.strip().replace(' ', '')  for line in fileH if not line[0] == '#' ]
    return terms

def getOperands(term):
    """go through term string to get the left-hand-side and right-hand-side operand, as well as the operator
    return LHS operand, RHS operand, and operator as strings """
    # find position to split operands
    pos = len(term)-1 
    if term[pos] != ')':
        RHSOperand = term[pos]
        operator = term[pos-1]
        LHSOperand = term[:pos-1]
    else:
        bracketCount = 1
        while bracketCount > 0:
            pos -= 1
            if term[pos] == '(':
                bracketCount -= 1
            elif term[pos] == ')':
                bracketCount += 1
        if pos == 0:
            LHSOperand = evaluateTerm(term[1:pos-1])
            operator = None
            RHSOperand = None
        else:
            LHSOperand = term[:pos-1]
            operator = term[pos-1]
            RHSOperand = term[pos+1:-1]
    return LHSOperand, RHSOperand, operator

def evaluateTerm(term):
    """evaluate the string of characters forming the term
    following the rules of the kid's math"""
    if len(term) == 1:
        return int(term[0])
    else:
        LHSOperand, RHSOperand, operator = getOperands(term)
        if operator == None:
            return LHSOperand
        if operator == '+':
            return evaluateTerm(LHSOperand) + evaluateTerm(RHSOperand)
        elif operator == '*':
            return evaluateTerm(LHSOperand) * evaluateTerm(RHSOperand)

""" PART 2: advanced math """

def evaluateTermAdv(term):
    """evaluate the string of characters forming the term
    following the rules of the kid's math"""
    #print("entering eval")
    #print(term)
    # if only one number in the term, return it as result
    if len(term) == 1:
        return int(term[0])
    else:
        # if there are no brackets, split along the *
        #  (least precendence) and calculate results
        if '(' not in term:
            if '*' not in term:
                return eval(term)
            else:
                return reduce(lambda a, b: a*b, [evaluateTermAdv(ter) for ter in term.split('*')])
        else:
            # if there are brackets, extract and evaluate the bracket,
            #  then replace with bracket value and continue
            openingPos = term.find('(')
            bracketCount = 1
            #print('opening',openingPos)
            closingPos = openingPos + 1
            while closingPos < len(term):
                if term[closingPos] == '(':
                    bracketCount += 1
                elif term[closingPos] == ')':
                    bracketCount -= 1
                if bracketCount == 0:
                    break
                closingPos += 1
            #print('closing',closingPos)
            bracketValue = evaluateTermAdv(term[openingPos+1:closingPos])
            newTerm = term[:openingPos] + str(bracketValue) + term[closingPos+1:]
            #print('newterm',newTerm)
            return evaluateTermAdv(newTerm)

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test18a"
    filename = "test18b"
    filename = "test18c"
    filename = "test18d"
    filename = "test18"
    filename = "input18"
    terms = loadTerms(filename)

    print('part 1: calculation all the terms and summing the results')
    results = [ evaluateTerm(term) for term in terms ]
    print('sum of results:', sum(results))

    print('\npart 2: using ADVANCED math!')
    resultsAdv = [ evaluateTermAdv(term) for term in terms ]
    print('sum of results:', sum(resultsAdv))

