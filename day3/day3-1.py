import fileinput
from collections import Counter
import re

inputArr = fileinput.input('day3\input.txt')

regexStr = "mul\([0-9]+,[0-9]+\)"

currCount = 0
for i, string in enumerate(inputArr):
    currInd = 0
    nextVal = re.search(regexStr, string)
    while(nextVal != None):
        span = nextVal.span()
        match = nextVal.group()
        currInd += span[1]
        lastDont = string[0:currInd].rfind("don't()")
        lastDo = string[0:currInd].rfind("do()")
        nextVal = re.search(regexStr, string[currInd + 1:])
        if lastDont == -1 or lastDont < lastDo:
            currCount += int(match[match.index('(') + 1 : match.index(',')]) * int(match[match.index(',') + 1 : -1])

print(currCount)
     