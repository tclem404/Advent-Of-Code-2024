import fileinput
from collections import Counter
import functools
import re

grid = [list(s.replace('\n','')) for s in list(fileinput.input('day12\input.txt'))]

hashMap = {}

for i, arr in enumerate(grid):
    for j, char in enumerate(arr):
        if char not in hashMap:
            hashMap[char] = set()
        hashMap[char].add((i,j))

regions = []
def defineRegions(i,j, region, currSet):
    if (i,j) in region:
        return
    region.add((i,j))
    grid[i][j] = 0
    if (i + 1, j) in currSet:
        defineRegions(i + 1, j, region, currSet)
    if (i - 1, j) in currSet:
        defineRegions(i - 1, j, region, currSet)
    if (i, j + 1) in currSet:
        defineRegions(i, j + 1, region, currSet)
    if (i, j - 1) in currSet:
        defineRegions(i, j - 1, region, currSet)

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 0:
            continue
        newRegion = set()
        defineRegions(i,j, newRegion, hashMap[grid[i][j]])
        regions.append(newRegion)

currSum = 0
for currSet in regions:
    area = len(currSet)
    perim = 0
    for i,j in currSet:
        if (i + 1, j) not in currSet:
            perim += 1
        if (i - 1, j) not in currSet:
            perim += 1
        if (i, j + 1) not in currSet:
            perim += 1
        if (i, j - 1) not in currSet:
            perim += 1 
    currSum += area * perim

print(currSum)