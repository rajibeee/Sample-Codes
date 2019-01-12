ar = raw_input()
a1= map(int, ar.split(" "))
#a1=[20, 23, 6]
b=a1[2]
a=[]
p1=a1[0]
p2=a1[1]
for j in range(p1,p2):
	c=p1
	a.append(c)
	if c==a1[1]:
		break
	else:
		c+=1
		p1+=1
		a.append(c)
		continue
a=list(set(a))
#print a

#b=6
count=0
for i in range(len(a)):
	a_rev=str(a[i])
	a_rev=int(a_rev[::-1])
	#print a_rev
	#print "abs(a[i]-a_rev)===", abs(a[i]-a_rev)
	num=abs(a[i]-a_rev)/float(b)
	#print num
	if num%1 == 0:
		count+=1
	else:
		continue

print count