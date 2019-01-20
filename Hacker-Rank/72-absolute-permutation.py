from copy import copy #This works but gets timeout :(
start=100
diff=2
final=[]
list2=[]
list1=[i for i in range(1,start+1)]

if diff==0:
	final=copy(list1)
else:
	list2=copy(list1)
	for i in range(len(list1)):
		try:
			for j in range(len(list2)):
				if abs(list1[i]-list2[j])==diff:
					final.append(list2[j])
					list2.remove(list2[j])
					break
				else:
					continue
		except IndexError:
			continue
if len(final)==start:
	for item in final:
		print item,
else:
	print "-1"