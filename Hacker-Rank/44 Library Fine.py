a=[1, 1, 2015]
b=[31, 12, 2014]

monthLate=a[1]-b[1]
yearLate=a[2]-b[2]
dayLate=a[0]-b[0]
#print monthLate
#print yearLate
if yearLate!=0:
	if yearLate<0:
		print 0
	else:
		print yearLate*10000
elif monthLate<0 or yearLate<0:
	print 0
elif monthLate==0 and yearLate==0:
	if dayLate<0:
		print 0
	else:
		print dayLate*15
elif yearLate==0 and monthLate!=0:
	#print monthLate
	print monthLate*500
elif monthLate==0 and yearLate==0:
	print dayLate*15 
	