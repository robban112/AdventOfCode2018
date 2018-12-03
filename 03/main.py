import numpy as np
from collections import namedtuple

Claim = namedtuple("Claim", "id fromleft fromtop width height")

class Cloth(object):
    def __init__(self):
        self.fabric = np.zeros((1000,1000))
    
    def addClaim(self,claim):
        for ind1 in range(claim.fromleft,claim.fromleft+claim.width):
            for ind2 in range(claim.fromtop,claim.fromtop+claim.height):
                self.fabric[ind1][ind2] += 1
    
    def countOverlaps(self):
        overlaps = 0
        for row in self.fabric:
            for inch in row:
                if inch > 1:
                    overlaps += 1
        return overlaps
    
    def checkIfClaimIsIntact(self,claim):
        for ind1 in range(claim.fromleft,claim.fromleft+claim.width):
            for ind2 in range(claim.fromtop,claim.fromtop+claim.height):
                if self.fabric[ind1][ind2] > 1:
                    return False
        return True

def parse_to_claim(str):
    spaces = str.split()
    fromleft = int(spaces[2].split(',')[0])
    fromtop = int(spaces[2].split(',')[1][:-1])
    width = int(spaces[-1].split('x')[0])
    height = int(spaces[-1].split('x')[1])
    return Claim(id=spaces[0], fromleft=fromleft, fromtop=fromtop,width=width, height=height)

def read():
    claims = []
    with open("input.txt") as f:
        for line in f.readlines():
            claims.append(parse_to_claim(line))
    return claims

def getCloth():
    claims = read()
    cloth = Cloth()
    for claim in claims:
        cloth.addClaim(claim)
    return cloth

def part1():
    cloth = getCloth()
    print(cloth.countOverlaps())

def part2():
    cloth = getCloth()
    for claim in read():
        if cloth.checkIfClaimIsIntact(claim):
            print(claim.id)
            return
part2()
