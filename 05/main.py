import string

def isOppositePolarity(char1, char2):
    if char1.lower() == char2.lower():
        if char1.islower() and char2.isupper():
            return True
        elif char1.isupper() and char2.islower():
            return True
    else:
        return False

def read():
    with open("input.txt") as f:
        return f.readlines()[0]

def reactPolymer(polymer):
    for index, char in enumerate(polymer[:-1]):
        if index > len(polymer)-2:
            break
        if (isOppositePolarity(polymer[index], polymer[index+1])):
            polymer = polymer.replace(polymer[index]+polymer[index+1], '')
    return polymer

def removeUnit(unit, polymer):
    polymer = polymer.replace(unit.lower(), '')
    polymer = polymer.replace(unit.upper(), '')
    return polymer

def fullyReactPolymer(polymer):
    lastPolymer = ""
    while True:
        polymer = reactPolymer(polymer)
        if len(polymer) == len(lastPolymer):
            break
        lastPolymer = polymer
    return polymer

def main1():
    polymer = read()
    lastPolymer = ""
    print(len(fullyReactPolymer(polymer)))

def main2():
    polymer = read()
    minReacted = polymer
    last = polymer
    for char in string.ascii_lowercase:
        reacted = fullyReactPolymer(removeUnit(char, polymer))
        if len(minReacted) > len(reacted):
            minReacted = reacted
    print(len(minReacted))

def test():
    polymer = 'AAaaBbCcDDEEeFf'
    reacted = polymer
    for char in ['a']:
        last = ""
        while True:
            reacted = reactWithUnit(char, reacted)
            if len(reacted) == len(last):
                break
            last = reacted
        print(reacted)
main2()