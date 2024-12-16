import fileinput
from collections import Counter
import functools
import re

lines = [s.replace('\n','') for s in list(fileinput.input('day14\input.txt'))]

pos = [[int(s[s.index('=') + 1:s.index(',')]), int(s[s.index(',') + 1:s.index(' ')])] for s in lines]
vel = [[int(s[s.rindex('=') + 1:s.rindex(',')]), int(s[s.rindex(',') + 1:])] for s in lines]

width = 101
height = 103

print("#" * 101)

currMoment = 0
seenPositions = set()
while True:
    positions = set()


    printThisLine = False
    counts = [0] * height
    for i in range(len(pos)):
        if tuple(pos[i]) not in positions:
            counts[pos[i][1]] += 1
            if counts[pos[i][1]] > 0.2 * width:
                printThisLine = True

        positions.add(tuple(pos[i]))
        pos[i] = [(pos[i][0] + vel[i][0]) % width, (pos[i][1] + vel[i][1]) % height]


    if currMoment % 10000 == 0:
        print(currMoment)

    if not printThisLine:
        currMoment += 1
        continue

    currLine = "\n\n\n\n\n\n\nSeconds Passed: " + str(currMoment) + '\n'
    currMoment += 1
    for j in range(height):
        for i in range(width):
            if (i,j) in positions:
                currLine += '#'
            else:
                currLine += ' '
        
        currLine += '\n'
    
    print(currLine)
    input()

