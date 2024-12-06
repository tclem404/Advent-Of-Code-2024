import fileinput
from collections import Counter
from functools import cmp_to_key
import re

grid = [s.replace('\n','') for s in list(fileinput.input('day6\input.txt'))]

currPos = [-1,-1]
direction = [-1, 0]

for i in range(len(grid)):
    if '^' in grid[i]:
        currPos = [i, grid[i].index('^')]
        break
print(currPos)

visited = set()
while True:
    visited.add(tuple(currPos))
    next = [currPos[i] + direction[i] for i in range(2)]
    if (next[0] < 0 or next[0] >= len(grid) or
        next[1] < 0 or next[1] >= len(grid[0])):
        break
    
    if grid[next[0]][next[1]] == '#':
        direction = [direction[1], -1 * direction[0]]
    else:
        currPos = next

print(len(visited))