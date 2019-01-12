def whoWillWin(a):
	aDi=abs(a[2]-a[0])
	bDi=abs(a[2]-a[1])
	if aDi<bDi:
		print "Cat A"
	elif aDi==bDi:
		print "Mouse C"
	else:
		print "Cat B"
			
n = int(raw_input())
for i in range(n):
	ar1 = raw_input()
	arr = map(int, ar1.split(" "))
	whoWillWin(arr)