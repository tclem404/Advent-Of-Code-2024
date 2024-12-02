import fileinput
from collections import Counter

inputArr = fileinput.input('day2\input.txt')

inputArr = [list(map(int, s.split(' '))) for s in inputArr]

modifiedArr = [[arr[j + 1] - arr[j] for j in range(len(arr) - 1)] for arr in inputArr]

import fileinput
from collections import Counter

inputArr = fileinput.input('day2\input.txt')

inputArr = [list(map(int, s.split(' '))) for s in inputArr]

possibleArrs = [[arr] + [[arr[i] for i in range(len(arr)) if i != j] for j in range(len(arr))] for arr in inputArr]
possibleArrs = [[[arr[j + 1] - arr[j] for j in range(len(arr) - 1)] for arr in arr2] for arr2 in possibleArrs]

def checkArr(arr):
    arr.sort()
    return not ((arr[0] < 0 and arr[-1] > 0) or abs(arr[0]) > 3 or abs(arr[-1]) > 3 or arr[0] == 0 or arr[-1] == 0)

currCount = 0
for i, arrOfArr in enumerate(possibleArrs):
    for arr in arrOfArr:
        if checkArr(arr):
            currCount += 1
            break
     

print(currCount)
     