import fileinput
from collections import Counter
import functools
import re

stones = [list(map(int, s.replace('\n','').split(' '))) for s in list(fileinput.input('day11\input.txt'))][0]

@functools.lru_cache(maxsize=None)
def splitStones(stone, blinks):
    if blinks == 0:
        return 1

    if stone == 0:
        return splitStones(1, blinks-1)
    
    if len(str(stone)) % 2 == 0:
        strStone = str(stone)
        return (splitStones(int(strStone[0: len(strStone) // 2]), blinks-1) +
                splitStones(int(strStone[len(strStone) // 2:]), blinks-1))
    
    return splitStones(stone*2024, blinks-1)

currSum = 0
for stone in stones:
    currSum += splitStones(stone, 75)

print(currSum)