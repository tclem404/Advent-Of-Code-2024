import fileinput
from collections import Counter

inputArr = fileinput.input('day2\input.txt')

inputArr = [list(map(int, s.split(' '))) for s in inputArr]

modifiedArr = [[arr[j + 1] - arr[j] for j in range(len(arr) - 1)] for arr in inputArr]

currCount = 0
for i, arr in enumerate(modifiedArr):
    arr.sort()
    if not ((arr[0] < 0 and arr[-1] > 0) or abs(arr[0]) > 3 or abs(arr[-1]) > 3 or arr[0] == 0 or arr[-1] == 0):
        currCount += 1

print(currCount)
     