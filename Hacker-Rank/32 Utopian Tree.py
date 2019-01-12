#f= int(raw_input())
#a=[]
#for i in range(f):
#	ar = int(raw_input())
#	a.append(ar)
#print a
a=[4,3]
h1=1
hlist=[]
hlist.append(h1)
for m in range(2,60):
	if m%2==0 and m!=0:
		h1=h1*2
	else:
		h1+=1
	#print "for ", m+1, "h1==",h1
	hlist.append(h1)
	
print hlist

for i in range(len(a)):
	print hlist[a[i]]