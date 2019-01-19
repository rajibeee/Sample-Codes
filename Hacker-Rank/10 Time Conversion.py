
listss=[]
h=0
sec=0
#s="06:40:03AM"
s = raw_input()
arr = map(str, s.split(":"))
listss.append(arr[2])
if "P" in listss[0]:
	h=int(arr[0])
	
	#print "PM"
	if h==12:
		h=12
	else:
		h=int(arr[0])+12
	sec=arr[2]
	#print s[0:2]
	
else:
	h=(arr[0])
	#print h
	if h=="12":
		h="00"
	else:
		h=(arr[0])
	sec=arr[2]
	#print "AM"

print('{0}:{1}:{2}'.format(h,arr[1],sec[0:2]))
