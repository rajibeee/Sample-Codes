tot=100
sCount= 1
sIndex=[0]
print len(sIndex)
distanceList=[]
for i in range(tot):
	temp=[]
	#for j in range(len(sIndex)):
	#	if sIndex.count(i)==0:
	#		diff=abs(i-sIndex[j])
	#		temp.append(diff)
	#		print "\n\ndistance from :" ,i, "to ", sIndex[j], "=", diff
	temp=[abs(i-sIndex[j]) for j in range(len(sIndex)) if sIndex.count(i)==0]
	print "temp = ", temp
	if len(temp)>1:
			mini=min(temp)
			distanceList.append(mini)
	elif len(temp)==1:
		distanceList.append(temp[0])
		
	else:
		continue
	
print "distanceList==",distanceList
if len(distanceList)==0:
	print 0
else:
	print max(distanceList)
	
###This is the shortest code---
sIndex.sort()
maxi=max(sIndex[0],tot-sIndex[-1]-1) #max value between "distance from first city to first space station
#and last city to last space station
for j in range(1,sCount): #loop over SS only
    dist=sIndex[j]-sIndex[j-1] #distance between SS
    maxi=max(dist//2,maxi) #compare with the previous maxi value
print maxi