#!/usr/bin/env python3

# advent of code, day 19
# oerms

import re

def getTestString(ruleNum, rules):
    """return test string from the rule dict for the given ruleNum"""
    rule = rules[ruleNum]
    if isinstance(rule, str):
        # if rule is single character, return said character
        return rule
    else:
        # if not, build regex from array, starting with opening bracket
        subrules = []
        for subrule in rule:
            subrules.append('(' + ''.join([ getTestString(nextrule, rules) for nextrule in subrule]) + ')')
        testString = '(' + '|'.join(subrules) + ')'

    if ruleNum == 0:
        # if we are at rule number 0: fix beginning and end of string and return
        testString = '^' + testString + '$'

    #print(testString)
    return testString

def countValidMessages(rules, messages):
    """validate data by rules and return number of valid data"""
    testString = getTestString(0, rules)
    print(testString)
    testRegex = re.compile(testString)

    valids = [ 1 for message in messages if testRegex.match(message)]
    #print(valids)

    return sum(valids)

def loadRulesMessages(filename):
    """load rules and messages from filename"""
    rules = dict()
    messages = []
    with open(filename) as fileH:
        for line in fileH:
            if line[0].isdigit():
                # if line begins with number, it is a rule:
                #  extract rule number and rule
                no, rule = line.strip().split(':')
                if rule[1] == '"':
                    rules[int(no)] = rule[2]
                    #print(int(no), rules[int(no)])
                    next
                else:
                    if '|' in rule:
                        rules[int(no)] = [[int(rul) for rul in part.split()] for part in rule.split('|')]
                        #print(int(no), rules[int(no)])
                    else:
                        rules[int(no)] = [[int(rul) for rul in rule.split()]]
                        #print(int(no), rules[int(no)])
            elif line.strip() == '':
                # skip empty line
                next
            else:
                # fill the messages array with messages
                messages.append(line.strip())
    return rules,messages 

if __name__ == "__main__":
    # change order of following for testcase
    filename = "test19a"
    filename = "test19b"
    filename = "input19"

    print('part 1: reading the input...')
    rules, messages = loadRulesMessages(filename)
    #print(rules)
    #print(messages)

    print('part 1: counting valid messages...')
    print('valid data:', countValidMessages(rules, messages))

    exit()

    print('part 2: setting the waypoints...')
    # using complex numbers...
    coord = complex(0)
    waypoint = complex(10 + 1j) # 1 == east, 1j == north, -1 == west, -1j == south

