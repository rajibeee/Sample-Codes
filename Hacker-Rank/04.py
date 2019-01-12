#!/bin/python

import math
import os
import random
import re
import sys
global n
#n=9
# Complete the diagonalDifference function below.
def diagonalDifference(r):
	second = sum(r[i][n-i-1] for i in range(n))
	first= sum(r[i][i] for i in range(n))
	return abs(first-second)
#r = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

#r=[[6, 6, 7, -10, 9, -3, 8, 9, -1],[9, 7, -10, 6, 4, 1, 6, 1, 1],[-1, -2, 4, -6, 1, -4, -6, 3, 9],
#[-8, 7, 6, -1, -6, -6, 6, -7, 2],[-10, -4, 9, 1, -7, 8, -5, 3, -5],[-8, -3, -4, 2, -3, 7, -5, 1, -5],[-2, -7, -4, 8, 3, -1, 8, 2, 3],
#[-3, 4,6, -7, -7, -8, -3, 9, -6],[-2, 0, 5, 4, 4, 4, -3, 3, 0]]

#print"r =", r
#print("A[1] =", r[0][2])      
#print("A[1][2] =", r[1][1])   
#print("A[0][-1] =", r[2][0])
n = int(raw_input())
arr = []
for _ in xrange(n):
	arr.append(map(int, raw_input().rstrip().split()))

result = diagonalDifference(arr)
print result
