import math
import os
import random
import re
import sys

n = int(raw_input())
#n=9
if 0 <= n <= 1000:
	k=n-2
	for i in range(1,n+1):
		print (" "*(n-i)+("#"*i))
		
else:
	pass
