import fileinput
from collections import Counter
import functools
import re

lines = [s.replace('\n','') for s in list(fileinput.input('day15\input.txt'))]
grid = list(map(list, lines[:lines.index("")]))

instructions = lines[lines.index("") + 1:]

startPos = [-1,-1]
for i, line in enumerate(grid):
    if '@' in line:
        startPos = [i, line.index('@')]
        grid[i][line.index('@')] = '.'
        break

print(startPos)


def mov(x, y, xDir, yDir):
    if grid[x][y] == '#':
        return -1
    
    if grid[x][y] == '.':
        return 1

    result = mov(x + xDir, y + yDir, xDir, yDir)
    
    if result != -1:
        grid[x + xDir][y + yDir] = grid[x][y]
    
    return result

for line in instructions:
    for movement in line:
        xDir = (movement == 'v') - (movement == '^')
        yDir = (movement == '>') - (movement == '<')

        result = mov(startPos[0] + xDir, startPos[1] + yDir, xDir, yDir)

        if result != -1:
            grid[startPos[0]][startPos[1]] = '.'
            
            startPos[0] += xDir
            startPos[1] += yDir

            grid[startPos[0]][startPos[1]] = '@'

currSum = 0
for i, line in enumerate(grid):
    currSum += sum([i * 100 + j for j in range(len(line)) if line[j] == 'O'])

print(currSum)