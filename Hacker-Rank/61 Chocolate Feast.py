n=10
cost=2
exc=5

def chocolateFeast(n, cost, exc):
	total=n//cost
	packets=total
	while packets>=exc:
		packets=packets-exc
		total+=1
		packets+=1
	print "total=== ",total,"packets=== ",packets
	
chocolateFeast(n, cost, exc)