

def read():
    inp = []
    with open("input.txt") as f: 
        for line in f.readlines():
            inp.append(line)
    return inp

def countChar(id, count):
    for char in id:
        if id.count(char) == count:
            return 1
    return 0
    
def part1():
    input = read()
    twoCount = 0
    threeCount = 0
    for id in input:
        twoCount += countChar(id, 2)
        threeCount += countChar(id, 3)
    print("Checksum: " + str(twoCount*threeCount))

def countSimilarities(first, second):
    d = 0
    for ind, char in enumerate(first):
        if second[ind] == char:
            continue
        elif d > 1:
            return
        else:
            d += 1
    if d == 1:
        return (first, second)
        
def part2():
    input = read()
    for id in input:
        for id2 in input:
            if id != id2:
                sim = countSimilarities(id, id2)
                if sim != None:
                    return sim

def main2():
    (first, second) = part2()
    chars = []
    for index, char in enumerate(first):
        if char == second[index]:
            chars.append(char)
    print(''.join(chars))
