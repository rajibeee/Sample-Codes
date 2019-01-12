from itertools import permutations
import random
maxi=0
#arr=[3, 2, 1, 3]
fake=raw_input()
s = raw_input()
arr = map(int, s.split())

maxi=max(arr)
print arr.count(maxi)
