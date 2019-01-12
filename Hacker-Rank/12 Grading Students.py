n = int(raw_input())
arr=[]
for i in range(n):
	s = int(raw_input())
	arr.append(s)
	

#print arr

for j in range(len(arr)):
	lastdigit = int(arr[j]%10)
	if arr[j]<38:
		arr[j]=arr[j]
	else:
		if lastdigit==5 or lastdigit==0:
			continue
		elif lastdigit==3 or lastdigit==4 or lastdigit==8 or lastdigit==9:
			if lastdigit==3 or lastdigit==4:
				arr[j]=arr[j]+(5-lastdigit)
			else:
				arr[j]=arr[j]+(10-lastdigit)
			#print "New number===", arr[j]
			
for k in range(len(arr)):

	print arr[k]