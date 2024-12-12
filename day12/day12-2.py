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
    sides = 0
    seenSides = set()
    for i,j in currSet:
        if (i + 1, j) not in currSet and (i,j, i+1,j) not in seenSides:
            sides += 1
            ind = 0
            while (i, j + ind) in currSet and (i + 1, j + ind) not in currSet:
                seenSides.add((i,j+ind,i+1,j+ind))
                ind += 1
            ind = 1
            while (i, j - ind) in currSet and (i + 1, j - ind) not in currSet:
                seenSides.add((i,j-ind,i+1,j-ind))
                ind += 1
        
        if (i - 1, j) not in currSet and (i,j, i-1,j) not in seenSides:
            sides += 1
            ind = 0
            while (i, j + ind) in currSet and (i - 1, j + ind) not in currSet:
                seenSides.add((i,j+ind,i-1,j+ind))
                ind += 1
            ind = 1
            while (i, j - ind) in currSet and (i - 1, j - ind) not in currSet:
                seenSides.add((i,j-ind,i-1,j-ind))
                ind += 1
        
        if (i, j + 1) not in currSet and (i,j, i,j+1) not in seenSides:
            sides += 1
            ind = 0
            while (i + ind, j) in currSet and (i + ind, j + 1) not in currSet:
                seenSides.add((i + ind,j,i + ind,j+1))
                ind += 1
            ind = 1
            while (i - ind, j) in currSet and (i -ind, j + 1) not in currSet:
                seenSides.add((i-ind,j,i-ind,j+1))
                ind += 1
        
        if (i, j - 1) not in currSet and (i,j, i,j-1) not in seenSides:
            sides += 1
            ind = 0
            while (i + ind, j) in currSet and (i + ind, j - 1) not in currSet:
                seenSides.add((i + ind,j,i + ind,j-1))
                ind += 1
            ind = 1
            while (i - ind, j) in currSet and (i -ind, j - 1) not in currSet:
                seenSides.add((i-ind,j,i-ind,j-1))
                ind += 1
        
    currSum += area * sides

print(currSum)