from itertools import combinations
#a=[1, 3, 2, 6, 1, 2]
#n=6
#k=3

ar2 = raw_input()
q = map(int, ar2.split(" ")) #d , m
n=q[0] #this is the summ
k=q[1]  #this is the number of piece

ar1 = raw_input()
a = map(int, ar1.split(" "))




comb=combinations(a,2)
final=[]
for i in list(comb):
	#print "combinations===",i
	summ=sum(list(i))
	if summ%k==0:
		#print "Perfect combinations===",i
		final.append(list(i))
		
print len(final)
		