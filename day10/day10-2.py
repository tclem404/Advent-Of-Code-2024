import fileinput
from collections import Counter
from functools import cmp_to_key
import re

grid = [list(map(int, s.replace('\n',''))) for s in list(fileinput.input('day10\input.txt'))]


currSum = 0
def pathFind(i,j):
    currNum = grid[i][j]
    if currNum == 9:
        return 1

    paths = 0
    if i + 1 < len(grid) and grid[i+1][j] == currNum + 1:
        paths += pathFind(i+1, j)
    if i - 1 >= 0 and grid[i-1][j] == currNum + 1:
        paths +=  pathFind(i-1, j)
    if j + 1 < len(grid[0]) and grid[i][j+1] == currNum + 1:
        paths += pathFind(i, j+1)
    if j - 1 >= 0 and grid[i][j-1] == currNum + 1:
        paths += pathFind(i, j-1)
    
    return paths

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            currSum += pathFind(i,j)

print(currSum)