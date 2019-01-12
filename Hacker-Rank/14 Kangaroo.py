a = raw_input()
arr = map(int, a.split(" "))
s1=arr[0]
d1=arr[1]
s2=arr[2]
d2=arr[3]
#s1=2564
#d1=5393
#s2=5121
#d2=2836
global r1
global r2
#global diff
diff=abs(s1-s2)
#print "first diff", diff
r1=s1+d1
r2=s2+d2
#print "\n1st jump -- first reach===",r1
#print " 1st jump -- second reach==",r2
diff1=abs(r2-r1)
#print "diff after ---1st jump==", diff1
closer=0

while True:
#for i in range(7):
	if d1==d2 and r1!=r2:
		#print "They are equal"
		print "NO"
		break
	elif r1==r2:
		print "YES"
		break
	r1+=d1
	r2+=d2
#	print "\n\n2nd jump --first reach===",r1
#	print "2nd jump --second reach==",r2
	diff=abs(r1-r2)
	if diff>diff1:
		#print "diif=",diff, "diff1==", diff1
		print "NO"
		break
	elif r1==r2:
		print "YES"
		break
	else:
		continue
		