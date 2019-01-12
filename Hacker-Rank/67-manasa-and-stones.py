from itertools import *
stones=4
diff1=10
diff2=100
list1=[diff1,diff2]
p=combinations_with_replacement(list1, (stones-1))

for perm in p:
	#print perm
	print (sum(list(perm))),