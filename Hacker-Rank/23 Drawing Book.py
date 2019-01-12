last=6
want=5
#last= int(raw_input())
#want = int(raw_input())
fromFirst=0
fromlast=0

if want==1 or want==last:
	print 0
elif want%2!=0 and last%2!=0:
	fromFirst=(want-1)/2
	fromlast=(last-want)/2
	print fromFirst
	print fromlast
	if fromFirst<fromlast:
		print fromFirst
	else:
		print fromlast
elif want%2==0 and last%2!=0:
	fromFirst=want/2
	fromlast=((last-1)-want)/2
	if fromFirst<fromlast:
		print fromFirst
	else:
		print fromlast
elif want%2==0 and last%2==0:
	fromFirst=want/2
	fromlast=((last-want)/2)
	if fromFirst<fromlast:
		print fromFirst
	else:
		print fromlast
		
elif want%2!=0 and last%2==0:
	fromFirst=(want-1)/2
	fromlast=(((last-1)-want)/2)
	if fromlast==0:
		fromlast=1
	if fromFirst<fromlast:
		print fromFirst
	else:
		print fromlast
		
	
	