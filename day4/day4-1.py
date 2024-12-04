import fileinput
from collections import Counter
import re

inputArr = [s.replace('\n','') for s in list(fileinput.input('day4\input.txt'))]

currCount = 0

forwardArr = [0,1,2,3]
backwardArr = [0,-1,-2,-3]
noneArr = [0,0,0,0]

def checkPos(i,j):
    words = 0

    forward = (j + 3 < len(inputArr[i]))
    backward = (j - 3 >= 0)
    up = (i - 3 >= 0)
    down = (i + 3 < len(inputArr))

    words += (forward and 
              (inputArr[i + noneArr[0]][ j + forwardArr[0]] +
               inputArr[i + noneArr[1]][ j + forwardArr[1]] +
               inputArr[i + noneArr[2]][ j + forwardArr[2]] +
               inputArr[i + noneArr[3]][ j + forwardArr[3]]) == "XMAS")
    words += (backward and 
              (inputArr[i + noneArr[0]][ j + backwardArr[0]] +
               inputArr[i + noneArr[1]][ j + backwardArr[1]] +
               inputArr[i + noneArr[2]][ j + backwardArr[2]] +
               inputArr[i + noneArr[3]][ j + backwardArr[3]]) == "XMAS")
    words += (down and backward and
              (inputArr[i + forwardArr[0]][ j + backwardArr[0]] +
               inputArr[i + forwardArr[1]][ j + backwardArr[1]] +
               inputArr[i + forwardArr[2]][ j + backwardArr[2]] +
               inputArr[i + forwardArr[3]][ j + backwardArr[3]]) == "XMAS")
    words += (up and backward and
              (inputArr[i + backwardArr[0]][ j + backwardArr[0]] +
               inputArr[i + backwardArr[1]][ j + backwardArr[1]] +
               inputArr[i + backwardArr[2]][ j + backwardArr[2]] +
               inputArr[i + backwardArr[3]][ j + backwardArr[3]]) == "XMAS")
    words += (down and forward and
              (inputArr[i + forwardArr[0]][ j + forwardArr[0]] +
               inputArr[i + forwardArr[1]][ j + forwardArr[1]] +
               inputArr[i + forwardArr[2]][ j + forwardArr[2]] +
               inputArr[i + forwardArr[3]][ j + forwardArr[3]]) == "XMAS")
    words += (up and forward and
              (inputArr[i + backwardArr[0]][ j + forwardArr[0]] +
               inputArr[i + backwardArr[1]][ j + forwardArr[1]] +
               inputArr[i + backwardArr[2]][ j + forwardArr[2]] +
               inputArr[i + backwardArr[3]][ j + forwardArr[3]]) == "XMAS")
    words += (up and
              (inputArr[i + backwardArr[0]][ j + noneArr[0]] +
               inputArr[i + backwardArr[1]][ j + noneArr[1]] +
               inputArr[i + backwardArr[2]][ j + noneArr[2]] +
               inputArr[i + backwardArr[3]][ j + noneArr[3]]) == "XMAS")
    words += (down and 
              (inputArr[i + forwardArr[0]][ j + noneArr[0]] +
               inputArr[i + forwardArr[1]][ j + noneArr[1]] +
               inputArr[i + forwardArr[2]][ j + noneArr[2]] +
               inputArr[i + forwardArr[3]][ j + noneArr[3]]) == "XMAS")

    return words
    



    
currCount = 0
for i in range(len(inputArr)):
    for j in range(len(inputArr[i])):
        currCount += checkPos(i,j)

print(currCount)