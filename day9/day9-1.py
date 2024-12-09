import fileinput
from collections import Counter
from functools import cmp_to_key
import re

nums = [s.replace('\n','') for s in list(fileinput.input('day9\input.txt'))]
nums = list(map(int, [s for s in nums[0]]))
lastInd = len(nums) - 1
currInd = 0
currPos = -1

checkSum = 0
while currInd <= lastInd:
    if nums[currInd] == 0:
        currInd += 1
        continue
    
    if nums[lastInd] == 0:
        lastInd -= 2
        continue

    currPos += 1
    nums[currInd] -= 1
    if currInd % 2 == 0:
        checkSum += currPos * (currInd // 2)
        continue
    
    nums[lastInd] -= 1
    checkSum += currPos * (lastInd // 2)

print(checkSum)