import fileinput
from collections import Counter
from functools import cmp_to_key
import re

lines = [s.replace('\n','') for s in list(fileinput.input('day8\input.txt'))]

antiNodes = set()
hashMap = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '.':
            continue

        if char in hashMap:
            for (x,y) in hashMap[char]:
                anti1 = (2 * x - i, 2 * y - j)
                anti2 = (2 * i - x, 2 * j - y)

                if (0 <= anti1[0] and
                    anti1[0] < len(lines) and
                    0 <= anti1[1] and
                    anti1[1] < len(lines[0])):
                    antiNodes.add(anti1)
                
                if (0 <= anti2[0] and
                    anti2[0] < len(lines) and
                    0 <= anti2[1] and
                    anti2[1] < len(lines[0])):
                    antiNodes.add(anti2)
            
            hashMap[char].append((i,j))

        else:
            hashMap[char] = [(i,j)]

print(len(antiNodes))