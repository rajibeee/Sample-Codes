#a=[2, 3, 4, 5, 6]

ar="1 2"
a= map(int, ar.split(" "))
count=0

try:
	count=0
	for i in range(len(a)):
		if a[i]%2!=0:
			a[i]+=1
			a[i+1]+=1
			count+=2
	print count
except IndexError:
	print "NO"

