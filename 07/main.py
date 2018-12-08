import numpy

def read():
    steps = []
    with open("input.txt") as f:
        for line in f.readlines():
            spaces = line.split()
            steps.append((spaces[1], spaces[7]))
    return steps

def getOrderDict():
    order = {}
    for inp in read():  
        if inp[0] in order:
            order[inp[0]].append(inp[1])
        else:
            order[inp[0]] = [inp[1]] 
    return order

def addNextAvailable(visited, lastStep, list1, list2):
    l = []
    for l2 in list2:
        if l2 not in list1 and l2 != lastStep and l2 not in visited:
            l.append(l2)
    return l

def getLastStep(order):
    for step in order:
        for nextStep in order[step]:
            if not nextStep in order:
                return nextStep

def getFirstsStep(order):
    firsts = []
    for key1 in order:
        isFirst = True
        for key2 in order:
            if key1 != key2:
                if key1 in order[key2]:
                    isFirst = False
        if isFirst:
            firsts.append(key1)
    return firsts

def getNextSteps(visible, visited, order):
    unlocked = []
    for v in visible:
        isUnlocked = True
        for o in order:
            if v in order[o] and not o in visited:
                isUnlocked = False
        if isUnlocked:
            unlocked.append(v)
    return unlocked

    
def stripIsWorkingOn(steps, currentTime, endTimes):
    freeSteps = []
    for step in steps:
        if step not in endTimes:
            freeSteps.append(step)
        else:
            if endTimes[step] <= currentTime:
                freeSteps.append(step)
    return freeSteps

def getFreeWorkers(workers, currentTime):
    freeWorkers = []
    for i in workers:
        if currentTime >= workers[i]:
            freeWorkers.append(i)
    return freeWorkers

def setIsBeingWorkedOn(nextSteps, freeWorkers, workers, currentTime, endTimes):
    for index, workerId in enumerate(freeWorkers):
        if index > len(nextSteps)-1:
            continue
        step = nextSteps[index]
        val = ord(step)-4
        endTimes[step] = currentTime+val
        workers[workerId] = currentTime+val
    return (workers, endTimes)  

def getIsWorkedOn(currentTimes, endTimes):
    workedOn = []
    for e in endTimes:
        if endTimes[e] > currentTimes:
            workedOn.append(e)
    return workedOn

def main2():
    order = getOrderDict()
    workers = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0
    }
    currentTime = 0
    endTimes = {}
    firsts = getFirstsStep(order)
    first = min(firsts)
    #firsts.remove(first)
    lastStep = getLastStep(order)
    order[lastStep] = []
    visible = firsts
    endTimes = {}
    currentTime = 0
    path = first
    isWorkedOn = [1]
    while len(isWorkedOn) > 0:
        for e in endTimes:
            if endTimes[e] == currentTime:
                print("order: " + str(order))
                visible += addNextAvailable(path, '', visible, order[e])
                print("visible is now: " + str(visible))
                path += e
        nextSteps = getNextSteps(visible, path, order)
        nextSteps = stripIsWorkingOn(nextSteps,currentTime,endTimes)
        freeWorkers = getFreeWorkers(workers, currentTime)
        print("free workers: " + str(freeWorkers))
        (workers, endTimes) = setIsBeingWorkedOn(nextSteps, freeWorkers, \
            workers, currentTime, endTimes)
        isWorkedOn = getIsWorkedOn(currentTime, endTimes)
        visible = list(filter(lambda x: not x in isWorkedOn, visible))
        print("current time : " + str(currentTime))
        print("is working on: " + str(isWorkedOn))
        print("workers: " + str(workers))
        print("end times: " + str(endTimes))
        print("visible: " + str(visible))
        currentTime+=1
    maxTime = 0
    for e in endTimes:
        if maxTime < endTimes[e]:
            maxTime = endTimes[e]
    print("time taken: " + str(maxTime))
        

def main1():
    order = getOrderDict()
    firsts = getFirstsStep(order)
    first = min(firsts)
    #firsts.remove(first)
    lastStep = getLastStep(order)
    visible = first
    path = first
    print("firsts: " + str(firsts))
    print("visible: " + str(visible))
    print("order: " + str(order))
    while len(visible) > 0:
        #print(visible, path, order, sep='\n')
        nextSteps = getNextSteps(visible, path, order)
        print("nextSteps: " + str(nextSteps))
        nextStep = min(nextSteps)
        visible.remove(nextStep)
        if nextStep in order:
            visible = addNextAvailable(path, lastStep, visible, order[nextStep])
        print("available next: " + str(visible) + " next step: " + str(nextStep))
        print("path: " + path)
        path += nextStep
    for key in order:
        if key not in path:
            print(key + " not in path!")
    print(path+lastStep)

main2()