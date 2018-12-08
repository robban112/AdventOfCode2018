
class Node(object):
    def __init__(self, numChilds, numMetadata, parentNode):
        self.childs = []
        self.metadata = []
        self.numMetadata = numMetadata
        self.numChilds = numChilds
        self.metadataIndex = 0
        self.parentNode = parentNode


    def metaDataIndexAdd(self, indexAdd):
        self.metadataIndex += indexAdd
    
def read():
    with open("input.txt") as f:
        return list(map(lambda x: int(x), f.read().split()))

def buildTree():
    inp = read()
    currentIndex = 2
    rootNode = Node(inp[0], inp[1], None)
    parentNode = rootNode
    currentNode = Node(inp[currentIndex], inp[currentIndex+1], parentNode)
    parentNode.childs.append(currentNode)

    currentIndex += 2
    while len(rootNode.childs) < rootNode.numChilds or len(rootNode.metadata) < rootNode.numMetadata:
        if currentNode.numChilds > len(currentNode.childs):
            parentNode = currentNode
            currentNode = Node(inp[currentIndex], inp[currentIndex+1], parentNode)
            parentNode.childs.append(currentNode)

            currentIndex+=2

        else:
            currentNode.metadata = inp[slice(currentIndex, currentIndex+currentNode.numMetadata)]
            currentIndex += currentNode.numMetadata
            if currentNode.parentNode != None:
                parentNode = currentNode.parentNode.parentNode
                currentNode = currentNode.parentNode
    return rootNode

def gatherMetaData(node, meta):
    meta += node.metadata
    if not node.childs:
        return meta
    else:
        for n in node.childs:
            gatherMetaData(n, meta)
    return meta

def getValue(node, val):
    if not node.childs:
        return val+sum(node.metadata)
    else:
        for m in node.metadata:
            if m <= len(node.childs):
                val = getValue(node.childs[m-1], val)
    return val

def main1():
    rootNode = buildTree()
    print(getValue(rootNode, 0))
    
main1()
