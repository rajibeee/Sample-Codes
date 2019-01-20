#this is in python3
def absolutePermutation(start, diff):
	Minus1=False
	perm = []
	if diff == 0:
		perm=[i for i in range(1,start+1)]
	elif (start/diff) % 2 != 0:
		Minus1= True
	else:
		add = True
		#perm = []  
		for i in range(1, start+1):
			if add:
				perm.append(i+diff)    
			else:
				perm.append(i-diff)    
			if i % diff == 0:
				if add:
					add = False
				else:
					add = True
	if Minus1:
		print ("-1")
	else:
		print (*perm)

t = int(input())

for t_itr in range(t):
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	absolutePermutation(n, k)