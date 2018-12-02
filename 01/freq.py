import collections
import time

changes = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        changes.append(int(line))


def duplicate(lista):
    dup = [item for item, count in collections.Counter(lista).items() if count > 1]
    if len(dup) > 0:
        return dup

def main():
    savedFrequencies = []
    freq = 0
    while True:
        for ch in changes:
            freq += ch
            if freq in savedFrequencies:
                print(freq)
                return
            savedFrequencies.append(freq)


main()
    






