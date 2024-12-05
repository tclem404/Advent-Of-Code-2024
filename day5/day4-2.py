import fileinput
from collections import Counter
from functools import cmp_to_key
import re

inputArr = [s.replace('\n','') for s in list(fileinput.input('day5\input.txt'))]

currCount = 0

rules = [list(map(int, s.split('|'))) for s in inputArr if len(s.split('|')) == 2]
rules = set(map(tuple, rules))

rows = [list(map(int, s.split(','))) for s in inputArr[inputArr.index("") + 1:]]

def compare(i,j):
    if (i,j) in rules:
        return 1
    elif (j,i) in rules:
        return -1

    return 0

for row in rows:
    correct = True
    for i, elem in enumerate(row):
        for j in range(i + 1, len(row)):
            if (row[j], elem) in rules:
                correct = False
                break
        
        if not correct:
            break
    
    if not correct:
        currCount += sorted(row, key=cmp_to_key(compare))[len(row)//2]


print(currCount)