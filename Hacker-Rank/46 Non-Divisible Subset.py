# Did not understand it that much..need revision
#a=[1, 7, 2, 4]
a=[19,10,12,10,24,25,22]
k=4
b=[]
b2=[]
a1=[]
a2=[]



residuals = [i %k for i in a]
counter = [0] * k
for r in residuals:
    counter[r] += 1
print residuals
# max one element with residual 0
c = min(counter[0], 1)
print "counter==",counter
print"\nc===",c
for i in range(1, (k//2)+1):  #Did not understand this for loop :(
    if i != k-i:
		print "counter[i]===",counter[i]
		print "counter[k-i]===",counter[k-i]
		c += max(counter[i], counter[k-i])
    else:
		print counter[i]
		c += min(counter[i], 1)
    
print(c)