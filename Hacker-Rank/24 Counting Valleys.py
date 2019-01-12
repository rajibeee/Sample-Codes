#m= int(raw_input())
#a= raw_input()

a="DDUUDDUDUUUD"
global alt
alt=0
alt_list=[]
counter=0
for i in range(len(a)):
	if a[i]=="U":
		alt=alt+1
		alt_list.append(alt)
	else:
		alt=alt-1
		alt_list.append(alt)

print alt_list
if -1 in alt_list:
	indices = [i for i, x in enumerate(alt_list) if x == -1]
	for j in range(len(indices)):
		if alt_list[indices[j]+1]==0:
			counter+=1
		else:
			continue
	
	print counter
else:
	print 0