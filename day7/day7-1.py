import fileinput
from collections import Counter
from functools import cmp_to_key
import re

lines = [list(map(int, s.replace('\n','').replace(':','').split(' '))) for s in list(fileinput.input('day7\input.txt'))]

currCount = 0

def checkVal(line, ind, currSum):
    if currSum > line[0]:
        return False
    if ind == len(line):
        return currSum == line[0]

    return (checkVal(line, ind + 1, currSum + line[ind]) or 
            checkVal(line, ind + 1, currSum * line[ind]))


for line in lines:
    if checkVal(line, 2, line[1]):
        currCount += line[0]


print(currCount)