from collections import namedtuple
import numpy
from datetime import datetime
from enum import Enum


Shift = namedtuple("Shift", "date minutesSlept")
Occurrence = namedtuple("Occurrence", "time guardState")

class GuardStateEnter(Enum):
    WOKEUP = 1
    WENTTOSLEEP = 2

class Guard(object):
    def __init__(self, id):
        self.shifts = []
        self.id = id
        self.timesSleptAtMinute = numpy.zeros(60)
    
    def addTimesSlept(self,timesSlept):
        self.timesSleptAtMinute += timesSlept

def minutesBetweenDates(date1, date2):
    return int(date1.time.split(':')[1]) - int(date2.time.split(':')[1])

def intervalSetToOne(timeSleptAtMinute, time1, time2):
    for i in range(time1, time2):
        timeSleptAtMinute[i] = 1
    return timeSleptAtMinute

def calculateTimeSlept(occurrences):
    timeSleptAtMinute = numpy.zeros(60)
    lastOccurrence = None
    for occurrence in occurrences:
        if occurrence.guardState == GuardStateEnter.WENTTOSLEEP:
            currentSleepTime = occurrence.time
        elif occurrence.guardState == GuardStateEnter.WOKEUP:
            currentWakeUpTime = occurrence.time
        
        if lastOccurrence != None:
            if lastOccurrence.guardState == GuardStateEnter.WENTTOSLEEP:
                timeSleptAtMinute = intervalSetToOne(timeSleptAtMinute, currentSleepTime, currentWakeUpTime)
        lastOccurrence = occurrence
    return timeSleptAtMinute

def calculateGuardsSlept(input):
    guards = {}
    occurrences = []
    currentGuard = None
    for inp in input:
        date = inp[0]
        info = inp[1]
        if "Guard" in info:
            if currentGuard != None:
                currentGuard.addTimesSlept(calculateTimeSlept(occurrences))

            id = int(info.split()[1][1:])
            if not id in guards:
                guards[id] = Guard(id)
            currentGuard = guards[id]
            occurrences = []
        elif "falls asleep" in info:
            occurrences.append(Occurrence(time=date.minute, guardState=GuardStateEnter.WENTTOSLEEP))
        elif "wakes up" in info:
            occurrences.append(Occurrence(time=date.minute, guardState=GuardStateEnter.WOKEUP))
    return guards

def readInputAndSort():
    inputs = []
    with open("input.txt") as f: 
        for line in f.readlines():
            spaces = line.split()
            time = datetime.strptime(spaces[0][1:] + " " + spaces[1][:-1], '%Y-%m-%d %H:%M')
            inputs.append((time, ' '.join(spaces[2:])))
    inputs.sort(key=lambda x: x[0])
    return inputs

def main():
    input = readInputAndSort()
    guardDict = calculateGuardsSlept(input)
    maxMin = 0
    for key in guardDict:
        guard = guardDict[key]
        for index, minute in enumerate(guard.timesSleptAtMinute):
            if minute > maxMin:
                maxMin = minute
                maxInd = index
                maxGuard = guard
    print(guardDict[1601].timesSleptAtMinute)
    print("MaxMin: " + str(maxMin) + " maxINdex " + str(maxInd) + " " + " guard: " + str(maxGuard.id))

main()