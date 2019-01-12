def angryProf(a1,c):
	k=int(a1[1])
	count=0
	for i in range(len(c)):
		if c[i]<=0:
			count+=1
		else:
			continue
	print type(k)
	print type(count)
	if (count<k):
		print "YES"
	elif (count==k):
		print "NO"
	else:
		print "NO"
		
loop= int(raw_input())
for i in range(loop):
	a1 = raw_input().split()
	ar = raw_input()
	c= map(int, ar.split(" "))
	angryProf(a1,c)
	
