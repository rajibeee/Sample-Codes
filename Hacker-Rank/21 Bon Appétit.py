ar1 = raw_input()
arr = map(int, ar1.split(" ")) 
print "arr[1]==",arr[1]
ar2 = raw_input()
a = map(int, ar2.split(" ")) 
sharedReal= int(raw_input())
didnoteat=a[arr[1]]
print "a==",a
print "sharedReal===",sharedReal
print "didnoteat===", didnoteat
#a=[3, 10, 2, 9]
#didnoteat=a[1]
#sharedReal=12

summ=sum(a)-didnoteat
sharedA=summ/2
print sharedA
if sharedA==sharedReal:
	print "Bon Appetit"
else:
	print abs(sharedA-sharedReal)