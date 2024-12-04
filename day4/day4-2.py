import fileinput
from collections import Counter
import re

inputArr = [s.replace('\n','') for s in list(fileinput.input('day4\input.txt'))]

currCount = 0

def checkPos(i,j):
    return (
        inputArr[i][j] == 'A' and
        (
            (inputArr[i-1][j-1] == 'M' or inputArr[i+1][j+1] == 'M') and 
            (inputArr[i-1][j-1] == 'S' or inputArr[i+1][j+1] == 'S') and
            inputArr[i-1][j-1] != inputArr[i+1][j+1]
        ) and
        (
            (inputArr[i+1][j-1] == 'M' or inputArr[i-1][j+1] == 'M') and 
            (inputArr[i+1][j-1] == 'S' or inputArr[i-1][j+1] == 'S') and
            inputArr[i+1][j-1] != inputArr[i-1][j+1]
        )
    )

    
currCount = 0
for i in range(1,len(inputArr)-1):
    for j in range(1,len(inputArr[i])-1):
        currCount += checkPos(i,j)

print(currCount)