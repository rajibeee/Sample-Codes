import string
ar="1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7"
a= map(int, ar.split(" "))
#print a
ar1="zaba"
ar1=" ".join(ar1)
b=map(str, ar1.split(" "))
#print b
alpha=list(string.ascii_lowercase)
#print alpha
w=[]
for i in range(len(b)):
	tempIndex=alpha.index(b[i])
	#print "Index for ", b[i],"=== ", tempIndex	
	w.append(a[tempIndex])
print max(w)*len(w)