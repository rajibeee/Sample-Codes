road=[2, 3, 1, 2, 3, 2, 3, 3]
eePoints=[4,6]
widList=[]
ind=eePoints[0]
for i in range((eePoints[1]-eePoints[0])+1):
	if ind<=eePoints[1]:
		temp=road[ind]
		widList.append(temp)
		ind+=1
	else:
		break

		
print min(widList)
	