from itertools import permutations
import random
listforsum=[]
mini=0
maxi=0
#arr=[1,3,5,7,9]
s = raw_input()
arr = map(int, s.split())

perm = permutations(arr, 4)  
for i in perm:
	k=sum(i)
	listforsum.append(k)
	mini=min(listforsum)
	maxi=max(listforsum)

#print(mini+" "+ maxi)
print('{0} {1}'.format(mini, maxi))
