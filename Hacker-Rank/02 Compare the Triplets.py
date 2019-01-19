#!/bin/python

import math
import os
import random
import re
import sys
p=[0,0]
# Complete the compareTriplets function below.
def compareTriplets(a, b):
	#print "a===", a
	#print "b===", b
    
	for i in range(3):
		if a[i]>b[i]:
			p[0]+=1
			#print "a bigger"
		elif a[i]==b[i]:
			pass
		else:
			#print "b bigger"
			p[1]+=1
    
   # print p
	return p

#print "a="
a = map(int, raw_input().rstrip().split())
#print "b="
b = map(int, raw_input().rstrip().split())

result = compareTriplets(a, b)

sarr = [str(a) for a in result]
print(" " . join(sarr))
