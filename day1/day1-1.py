import fileinput
from collections import Counter

inputArr = fileinput.input('day1\input.txt')

inputArr = [[int(s.split(' ')[0]), int(s.split(' ')[-1])] for s in inputArr]
list1 = [arr[0] for arr in inputArr]
list1.sort()
list2 = [arr[1] for arr in inputArr]
list2.sort()


list2 = Counter(list2)

print(sum([list1[i] * list2[list1[i]] for i in range(len(list1)) if list1[i] in list2]))