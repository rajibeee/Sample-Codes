chCount=5
max=3  
arr=[4, 2, 6, 1, 10]
dict={}
pageList=[]
for i in range(chCount): # This calculates which chapter will need how many pages
	pageCount=0
	if arr[i]>max:
		pageCount+=arr[i]//max
		#print "\n\npageCount for---1----", arr[i], "is ", pageCount
		if (arr[i]%max)<max and (arr[i]%max)>0 :
			pageCount+=1
		#	print "pageCount for----2----", arr[i], "is ", pageCount
		elif arr[i]%max==0:
			pageCount=arr[i]//max
		#	print "pageCount for----3---", arr[i], "is ", pageCount
	if arr[i]<=max:
		pageCount=1
		#print "pageCount for------4----", arr[i], "is ", pageCount
	#print "\n\npageCount for", arr[i], "is ", pageCount
	pageList.append(pageCount)
	
#print pageList # This is not needed for the problem solution

page=1
special=0
for p in arr:
    start = 1
    while True:
		firstPage, lastPage = start, min(start+max-1,p)
		#print "fp==", fp, "lp=== ",lp
		if firstPage <= page <= lastPage:
			print "firstPage==", firstPage, "lastPage=== ",lastPage
			special += 1
		page += 1
		if (start+max > p):
			break
		else:
			start += max
print(special)