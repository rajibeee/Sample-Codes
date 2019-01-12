from itertools import permutations

#given="dcbb"
given="0125330"
asciList=[]
perms = list(set([''.join(p) for p in permutations(given)]))
perms.sort()
print perms
try:
	ind= perms.index(given)+1
	print perms[ind]
except IndexError:
	print "no answer"
'''
This one works but----
have to implement the following to be quick
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
'''