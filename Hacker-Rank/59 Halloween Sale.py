cost=20
d=3
mini=6 
total=80
def hallSale(cost,d,mini,total):
	count=1
	loop=(total-cost)/d
	total-=cost
	print "total==1== ",total,"cost== ",cost, "Count= ",count
	#print loop
	for i in range(loop):
		cost=cost-d
		total-=cost
		count+=1
		if cost>mini and total>=mini:
			
			print "total==2== ",total, "cost== ",cost,"Count= ",count
		elif total<=mini:
			total+=cost
			count-=1
			print "total==3== ",total, "cost== ",cost,"Count= ",count
			print "here"
			break
		elif cost<mini:
			total+=cost
			count-=1
			print "total==4== ",total, "cost== ",cost,"Count= ",count
			print "here 2"
			break
	
	if total<mini:
		print "total==5== ",total, "cost== ",cost,"Count= ",count
		print count
	else:
		print "total==6== ",total, "cost== ",cost,"Count= ",count
		if total<cost:
			print count
		else:
			print (total//mini)+count

if cost>total:
	print 0
else:
	hallSale(cost,d,mini,total)