from itertools import combinations
ar=raw_input() 
inp1= map(int, ar.split(" "))
loop=inp1[0]
numberoftopic=inp1[1]
a=[]
for m in range(loop):
    ar1=raw_input() 
    a.append(ar1)
	
#a=['10101','11100','11010','00101']
topicCounterList=[]
$numberoftopic=5
a1=combinations(a, 2)
for i in list(a1):
	print i
	knownTopics=0
	a2=list(i)
	x=int(str(a2[0]), 2) #Converting so that we can do bitwise operation
	y=int(str(a2[1]), 2)
	knownTopics= bin((x|y)).count('1') #counting 1 after bitwise OR
	topicCounterList.append(knownTopics)
maxTopics=max(topicCounterList)
print maxTopics
print topicCounterList.count(maxTopics)