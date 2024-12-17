import fileinput
from collections import Counter
import functools
import re

lines = [s.replace('\n','') for s in list(fileinput.input('day15\input.txt'))]
grid = lines[:lines.index("")]

grid = list(map(list, [l.replace('#', "##").replace('O', "[]").replace('.', "..").replace('@', "@.") for l in grid]))


instructions = lines[lines.index("") + 1:]

startPos = [-1,-1]
for i, line in enumerate(grid):
    if '@' in line:
        startPos = [i, line.index('@')]
        break


def check(x, y, xDir, yDir, partner):
    if grid[x][y] == '#':
        return False
    
    if grid[x][y] == '.':
        return True

    result1 = check(x + xDir, y + yDir, xDir, yDir, True)

    if yDir == 0 and partner:
        if result1 and grid[x][y] == ']':
            return check(x, y - 1, xDir, yDir, False)
        if result1 and grid[x][y] == '[':
            return check(x, y + 1, xDir, yDir, False)
    
    return result1

def mov(x, y, xDir, yDir):
    if grid[x][y] == '#':
        return
    
    if grid[x][y] == '.':
        return
    
    mov(x + xDir, y + yDir, xDir, yDir)
    grid[x + xDir][y + yDir] = grid[x][y]
    prev = grid[x][y]
    grid[x][y] = '.'

    if xDir != 0:
        if prev == '[':
            mov(x, y + 1, xDir, yDir)
        if prev == ']':
            mov(x, y - 1, xDir, yDir)

for line in instructions:
    for movement in line:

        xDir = (movement == 'v') - (movement == '^')
        yDir = (movement == '>') - (movement == '<')

        result = check(startPos[0] + xDir, startPos[1] + yDir, xDir, yDir, True)

        if result:
            mov(startPos[0], startPos[1], xDir, yDir)
            startPos = [startPos[0] + xDir, startPos[1] + yDir]


for line2 in grid:
    print(''.join(line2))

currSum = 0
for i, line in enumerate(grid):
    currSum += sum([i * 100 + j for j in range(len(line)) if line[j] == '['])

print(currSum)