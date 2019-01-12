import math  #Not complete
def calculateDistance(a,b):  
     dist = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)  
     return int(dist)  
	 
pos=[4,4]
#block=[[3,2],[5,5],[2,4]]
block=[[8,1]]
board=8
counter=0

print calculateDistance(pos,[1,4])

for i in range(len(block)):
	if pos[1]==block[i][1] or pos[0]==block[i][0]: #straight ones
		counter+=calculateDistance(pos, block[i])
		counter-=1 #as you can not reach the blocked court
		print "counte---1---",counter
	else:
		temp=[board,pos[1]]
		counter+=calculateDistance(pos,temp)
		print "counte---2---",counter
		temp=[pos[0],board]
		counter+=calculateDistance(pos,temp)
		print "counte---3---",counter
		temp=[pos[0],1]
		counter+=calculateDistance(pos,temp)
		print "counte---4---",counter
		temp=[1,pos[1]]
		counter+=calculateDistance(pos,temp)
		print "counte---5---",counter
		
	if abs(pos[0]-block[i][0])== abs(pos[1]-block[i][1]): #Diagonal Ones
		counter+=calculateDistance(pos, block[i])
		counter-=1 #as you can not reach the blocked court
		print "counte---6---",counter
	else:
		a=min(abs(pos[0]-board),abs(pos[1]-1)) #right-down
		temp=[pos[0]+a,pos[1]-a]
		counter+=calculateDistance(pos,temp)
		print "counte---7---",counter
		b=min(abs(pos[0]-board),abs(pos[1]-board)) #right-UP
		temp=[pos[0]+b,pos[1]+b]
		counter+=calculateDistance(pos,temp)
		print "counte---8---",counter
		
		
print counter