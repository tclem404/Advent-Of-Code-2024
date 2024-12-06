import fileinput
from collections import Counter
from functools import cmp_to_key
import re

grid = [list(s.replace('\n','')) for s in list(fileinput.input('day6\input.txt'))]

startPos = [-1,-1]

for i in range(len(grid)):
    if '^' in grid[i]:
        startPos = [i, grid[i].index('^')]
        break

DryRun = set()
currPos = startPos
direction = [-1, 0]
while True:
    DryRun.add(tuple(currPos))
    next = [currPos[i] + direction[i] for i in range(2)]
    if (next[0] < 0 or next[0] >= len(grid) or
        next[1] < 0 or next[1] >= len(grid[0])):
        break
    
    if grid[next[0]][next[1]] == '#':
        direction = [direction[1], -1 * direction[0]]
    else:
        currPos = next

currCount = 0
for i,j in DryRun:
    if [i,j] == startPos or grid[i][j] == '#':
        continue

    grid[i][j] = '#'
    currPos = startPos
    direction = [-1, 0]
    visited = set()
    while True:
        uniqueKey = (currPos[0], currPos[1], direction[0], direction[1])
        if uniqueKey in visited:
            currCount += 1
            break

        visited.add(uniqueKey)
        next = [currPos[i] + direction[i] for i in range(2)]
        if (next[0] < 0 or next[0] >= len(grid) or
            next[1] < 0 or next[1] >= len(grid[0])):
            break
        
        if grid[next[0]][next[1]] == '#':
            direction = [direction[1], -1 * direction[0]]
        else:
            currPos = next
    
    grid[i][j] = '.'

print(currCount)