ar = raw_input()
a1= map(int, ar.split(" "))
n=a1[0]
rot=a1[1]
q=a1[2]
ar1 = raw_input()
a= map(int, ar1.split(" "))
a = a[n-(rot%n):n]+a[0:n-(rot%n)]
#a=[1, 2, 3]
#for i in range(rot):
#	a.insert(0, a[-1])
#	a=a[:-1]
	#print a

for i in range(q):
	ind = int(raw_input())
	print a[ind]
