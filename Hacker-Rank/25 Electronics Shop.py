#b=10
#n=2
#m=3
#k=[3, 1]
#d=[5, 2, 8]

ar1 = raw_input()
arr = map(int, ar1.split(" ")) 
b=arr[0]
n=arr[1]
m=arr[2]

ar2 = raw_input()
k = map(int, ar2.split(" ")) 

ar3 = raw_input()
d = map(int, ar3.split(" ")) 

cost_list=[]
for i in range(len(k)):
	if min(k)>=b:
		print -1
	for j in range(len(d)):
		if min(d)>=b:
			print -1
		cost=k[i]+d[j]
		if cost<=b:
			cost_list.append(cost)

print max(cost_list)