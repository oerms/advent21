#!/usr/bin/env python3

# advent of code, day 7
# oerms

def getRulefromLine(line: str):
    """extract baggage rule from single line"""
    splitline = line.split()
    bag = splitline[0] + ' ' + splitline[1]
    if splitline [4] == 'no':
        return {bag: dict()}
    splitline = splitline[4:]
    content = dict()
    while splitline != []:
        content.update({splitline[1] + ' ' + splitline[2]:int(splitline[0])})
        splitline = splitline[4:]
    return {bag:content}

def loadRules(filename):
    """load rules from filename"""
    rules = dict()
    with open(filename) as fileH:
        for line in fileH:
            rules.update(getRulefromLine(line))
    return rules

def testForColor(rules, bag, finalColor):
    """test bag, whether it can contain eventually a bag of finalColor"""
    if finalColor in rules[bag]:
        return 1
    else:
        for nextBag in rules[bag]:
            if testForColor(rules, nextBag, finalColor) == 1:
                return 1
            else:
                continue
        return 0

if __name__ == "__main__":
    filename = "test7"
    filename = "input7"
    rules = loadRules(filename)

    bagsWithShiny = 0
    for bag in rules:
        bagsWithShiny += testForColor(rules, bag, "shiny gold")
    print('number of bags, which can hold a shiny gold bag:',bagsWithShiny)


