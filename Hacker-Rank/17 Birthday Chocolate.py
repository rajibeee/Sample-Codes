from itertools import combinations

#ar = raw_input()
#ar1 = raw_input()
#s = map(int, ar1.split(" "))

#ar2 = raw_input()
#q = map(int, ar2.split(" ")) #d , m
#d=q[0] #this is the summ
#m=q[1]  #this is the number of piece
s=[2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
m=7
d=18
print "s=",s
print "\nm====",m
print "\nd==",d
#comb=combinations(s,m)
final=[]
#for i in list(comb):
#	#print "combinations===",i
#	summ=sum(list(i))
#	if summ==d:
#		print "Perfect combinations===",i
#		final.append(sorted(list(i)))

for i in range(len(s)):
	#print "Slice in consideration===", s[i:i+m]
	summ=sum(s[i:i+m])
	if summ==d:
		print "Perfect combinations===",s[i:i+m]
		final.append(s[i:i+m])
	


print "final====",final
#final=final.sort()
#print final
def purge_dublicates(X):
    unique_X = []
    for i, row in enumerate(X):
        if row not in X[i + 1:]:
            unique_X.append(row)
    return unique_X

print purge_dublicates(final)
print len(purge_dublicates(final))