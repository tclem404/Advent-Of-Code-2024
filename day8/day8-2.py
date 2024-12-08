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
                jump = (x-i, y-j)
                jumps = 0

                while True:
                    anti1 = (x - jumps*jump[0], y - jumps*jump[1])
                    anti2 = (x + jumps*jump[0], y + jumps*jump[1])
                    jumps += 1
                    added = False
                    if (0 <= anti1[0] and
                        anti1[0] < len(lines) and
                        0 <= anti1[1] and
                        anti1[1] < len(lines[0])):
                        antiNodes.add(anti1)
                        added = True
                    
                    if (0 <= anti2[0] and
                        anti2[0] < len(lines) and
                        0 <= anti2[1] and
                        anti2[1] < len(lines[0])):
                        antiNodes.add(anti2)
                        added = True
                    
                    if not added:
                        break
            
            hashMap[char].append((i,j))

        else:
            hashMap[char] = [(i,j)]

print(len(antiNodes))