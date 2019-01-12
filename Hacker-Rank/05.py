#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
	neg=0
	pos=0
	zero=0
	for i in range (len(arr)):
		if arr[i]<0:
			neg+=1;
		elif arr[i]>0:
			pos+=1;
		else:
			zero+=1;
			
	#print "neg=", neg
	#print "pos==", pos
	#print "zero==", zero
	lenn=len(arr)
	neggo=(float(neg)/float(lenn))
	posso=float(pos)/float(lenn)
	zroo=float(zero)/float(lenn)
	newarr=[posso,neggo,zroo]
	#print newarr
	return newarr

n = int(raw_input())
#n=6
#arr=[-4, 3, -9, 0, 4, 1]

arr = map(int, raw_input().rstrip().split())

res=plusMinus(arr)
print "%.6f"% res[0]
print "%.6f"% res[1]
print "%.6f"% res[2]
