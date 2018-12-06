import numpy 
import operator

infinity = 9999999
gridsizeX = 354
gridsizeY = 354

def read():
    nodes = []
    with open("input.txt") as f: 
        for index, line in enumerate(f.readlines()):
            p = line.strip().split(', ')
            nodes.append((index, int(p[0]), int(p[1])))
    return nodes

def distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def pointToString(point1):
    return str(point1[0]) + " " + str(point1[1])

def minDistToNode(point, nodes):
    minNode = nodes[0]
    distMin = 100000000000
    distances = []
    for node in nodes:
        distances.append((node, distance(point, (node[1], node[2]))))
    distances.sort(key=lambda x: x[1])
    if distances[0][1] == distances[1][1]:
        return None
    return distances[0][0][0]

def initGrid(nodes):
    grid = numpy.zeros((gridsizeX,gridsizeY))
    for x in range(0,gridsizeX):
        for y in range(0,gridsizeY):
            indexOfMinDist = minDistToNode((x,y), nodes)
            if indexOfMinDist != None:
                grid[x][y] = indexOfMinDist
            else:
                grid[x][y] = -1
    return grid

def initCount(grid, nodes):
    count = {}
    for c in nodes:
        count[c[0]] = 0
    for row_index, row in enumerate(grid):
        for element_index, el in enumerate(row):
            if el != -1:
                if row_index == 0 or row_index == gridsizeY-1 or element_index == 0 \
                    or element_index == gridsizeX-1:
                    count[el] = infinity
                else:
                    count[el] += 1
    return count

def main1():
    nodes = read()
    grid = initGrid(nodes)
    count = initCount(grid, nodes)
    maxCount = 0
    maxNode = None
    for c in count:
        if count[c] > maxCount and count[c] < infinity:
            maxCount = count[c]
            maxNode = nodes[c]
    print("maxnode: " + str(maxNode))
    print(str(maxNode[1]) + ", " + str(maxNode[2]) + " count: " + str(maxCount))

def underThresh(grid, nodes):
    underThresGrid = numpy.zeros((gridsizeX, gridsizeY))
    for index1, row in enumerate(grid):
        for index2, el in enumerate(row):
            total = 0
            for node in nodes:
                total += distance((index1,index2), (node[1], node[2]))
            underThresGrid[index1][index2] = total < 10000
    return underThresGrid
                             
def main2():
    nodes = read()
    grid = initGrid(nodes)
    count = initCount(grid, nodes)
    print(underThresh(grid, nodes).sum())


main2()