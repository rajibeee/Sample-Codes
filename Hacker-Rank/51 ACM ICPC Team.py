from itertools import combinations
ar=raw_input() 
inp1= map(int, ar.split(" "))
loop=inp1[0]
numberoftopic=inp1[1]
a=[]
for m in range(loop):
    ar1=raw_input() 
    temp=" ".join(ar1)
    a_ind= map(int, temp.split(" "))
    a.append(a_ind)

topicCounterList=[]
a1=combinations(a, 2)
for i in list(a1):
    knownTopics=0
    a2=list(i)
    for j in range(numberoftopic):
        if a2[0][j]==1 or a2[1][j]==1:
            knownTopics+=1
    topicCounterList.append(knownTopics)
maxTopics=max(topicCounterList)
print maxTopics
print topicCounterList.count(maxTopics)