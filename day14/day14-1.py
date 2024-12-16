import fileinput
from collections import Counter
import functools
import re

lines = [s.replace('\n','') for s in list(fileinput.input('day14\input.txt'))]

pos = [[int(s[s.index('=') + 1:s.index(',')]), int(s[s.index(',') + 1:s.index(' ')])] for s in lines]
vel = [[int(s[s.rindex('=') + 1:s.rindex(',')]), int(s[s.rindex(',') + 1:])] for s in lines]

width = 101
height = 103

tl = 0
tr = 0
bl = 0
br = 0

for (x,y), (xVel, yVel) in zip(pos, vel):
    endPos = ((x + 100 * xVel) % width, (y + 100 * yVel) % height)

    tl += (endPos[0] < (width - 1) // 2 and endPos[1] < (height - 1) // 2)
    tr += (endPos[0] > (width - 1) // 2 and endPos[1] < (height - 1) // 2)
    bl += (endPos[0] < (width - 1) // 2 and endPos[1] > (height - 1) // 2)
    br += (endPos[0] > (width - 1) // 2 and endPos[1] > (height - 1) // 2)

print(tl * tr * bl * br)