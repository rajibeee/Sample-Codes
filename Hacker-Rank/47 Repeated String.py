arr="gfcaaaecbg"
n=547602
leng=len(arr)
count1=arr.count("a")
print count1
a1=n//leng
rem=n%leng
print a1,rem
count2=arr[0:rem].count("a")
if count1==0:
	print 0
else:
	print a1*count1+count2