a=[0, 0, 1, 0, 0, 1, 0]
leng=len(a)-1
avoid= [i for i, x in enumerate(a) if x == 1]
print avoid
global reached
reached=0
jumpcount=0
print leng
while reached<leng:
	reached+=2
	jumpcount+=1
	print "Reached1= ", reached, "jumpcount= ",jumpcount
	if reached==leng:
		print "finished"
		break
	elif avoid.count(reached)==1:
		reached-=1
		print "Reached2= ", reached, "jumpcount= ",jumpcount
		continue
	elif leng-reached==1:
			reached+=1
			jumpcount+=1
			print "Reached3= ", reached, "jumpcount= ",jumpcount
			break
	
	
print jumpcount