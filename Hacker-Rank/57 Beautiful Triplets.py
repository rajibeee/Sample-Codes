d=3
#arr=[1,6, 7, 7, 8, 10, 12, 13, 14, 19]
arr=[1, 2, 4, 5, 7, 8, 10]
cnt=0
for i in arr[:-2]:
	print "\ni+d== ",i+d, "and i+d+d== ", i+d+d
	if i+d in arr and i+d+d in arr:
		cnt+=1

print cnt