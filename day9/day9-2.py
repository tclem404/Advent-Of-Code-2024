import fileinput
from collections import Counter
from functools import cmp_to_key
import re

nums = [s.replace('\n','') for s in list(fileinput.input('day9\input.txt'))]
nums = list(map(int, [s for s in nums[0]]))

currInd = 0
gaps = [] # start pos, len
files = [] # start pos, len, val

for i, num in enumerate(nums):
    if i % 2 == 0 and num != 0:
        files.append([currInd, num, i // 2])
    elif i % 2 == 1 and num != 0:
        gaps.append([currInd, num])
    currInd += num

files = files[::-1]

for i, file in enumerate(files):
    for j in range(len(gaps)):
        if gaps[j][0] > file[0]:
            break

        if gaps[j][1] < file[1]:
            continue
            
        file[0] = gaps[j][0]
        gaps[j][0] += file[1]
        gaps[j][1] -= file[1]

        if gaps[j][1] == 0:
            gaps.pop(j)
        
        break

checkSum = 0
for file in files:
    for i in range(file[0], file[0] + file[1]):
        checkSum += file[2] * i
print(checkSum)