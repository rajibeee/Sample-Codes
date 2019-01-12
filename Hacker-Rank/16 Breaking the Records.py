#a=[10, 5, 20, 20, 4, 5, 2, 25, 1]
a=[3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
#ar = raw_input()
#ar1 = raw_input()
#a = map(int, ar1.split(" "))
print a
count_max=0
count_min=0
max=a[0]
min=a[0]
for i in range(1,len(a)):	
	if a[i]>max:
		max=a[i]
		count_max+=1
	elif a[i]<min:
		min=a[i]
		count_min+=1
	else:
		continue
print count_max, count_min