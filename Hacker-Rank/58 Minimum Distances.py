#n = int(raw_input())
#arr = map(int, raw_input().rstrip().split())
#arr=[7, 1, 3, 4, 1, 7]
arr=[1, 2, 3, 4, 10]
#arr=[3,2,1,2,3]
finalList=[]

for j in range(len(arr)):
	indices=[]
	indices = [i for i, x in enumerate(arr) if x == arr[j]]
	print indices
	if len(indices)==2:
		diff=abs(indices[0]-indices[1])
		finalList.append(diff)
finalList=list(set(finalList))
if len(finalList)==0:
	print -1
else:
	print min(finalList)