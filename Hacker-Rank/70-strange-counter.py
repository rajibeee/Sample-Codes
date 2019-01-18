start=3
target=1000
while target > start:
	target = target-start
	start *= 2
	print "\nstart===",start, "t=== ", target

print "\nstart===",start, "t=== ", target
print(start-target+1)