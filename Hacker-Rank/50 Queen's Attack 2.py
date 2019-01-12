pos=[3,4]
block=[[3,2],[5,5],[2,4]]
board=5
att=[]
temp1=pos[0]+1
temp2=pos[1]+1
temp3=pos[1]-1
temp4=pos[0]-1

for i in range(1,board+1):
	if temp1<=board:
		new_pos=[temp1,pos[1]]
		print "\n new_pos===1== ",new_pos
		if block.count(new_pos)==1:
			break
		else:
			att.append(new_pos)
		temp1+=1
	elif temp1>board:
		pass
for i in range(1,board+1):
	if temp2<=board:
		new_pos=[pos[0],temp2]
		print "\n new_pos===2=== ",new_pos
		if block.count(new_pos)==1:
			break
		else:
			att.append(new_pos)
		temp2+=1
	elif temp2>board:
		pass
for i in range(1,board+1):
	if temp3>=1:
		new_pos=[pos[0],temp3]
		print "\n new_pos===3=== ",new_pos
		if block.count(new_pos)==1:
			print "\n\n\n ---Breaking ---new_pos== ", new_pos
			break
		else:
			att.append(new_pos)
		temp3-=1
	elif temp3<1:
		pass
for i in range(1,board+1):
	print "temp4 ==== ", temp4
	if temp4>=1:
		new_pos=[temp4,pos[1]]
		print "\n new_pos===4=== ",new_pos
		if block.count(new_pos)==1:
			print "\n\n\n ---Breaking ---new_pos== ", new_pos
			break
		else:
			att.append(new_pos)

		temp4-=1
	elif temp4<1:
		pass

temp1=pos[0]+1
temp2=pos[1]+1
temp3=pos[0]-1
temp4=pos[1]-1
for i in range(1,board+1):
		#Corners
	if temp1<=board and temp2<= board:
		new_pos=[temp1,temp2]
		print "\n new_pos===5=== ",new_pos
		if block.count(new_pos)==1:
			break
		else:
			att.append(new_pos)
		temp1+=1
		temp2+=1
	elif temp1>board or temp2> board:
		break
for i in range(1,board+1):
	if temp3>=1 and temp4>= 1:
		new_pos=[temp3,temp4]
		print "\n new_pos===6=== ",new_pos
		if block.count(new_pos)==1:
			break
		else:
			att.append(new_pos)

		temp3-=1
		temp4-=1
	elif temp3<1 or temp4<1:
		break

temp1=pos[0]+1
temp2=pos[1]-1

temp3=pos[0]-1
temp4=pos[1]+1
for i in range(1,board+1):
	if temp1<=board and temp2>= 1:
		new_pos=[temp1,temp2]
		print "\n new_pos===7=== ",new_pos
		if block.count(new_pos)==1:
			break
		else:
			att.append(new_pos)
		temp1+=1
		temp2-=1
	elif temp1>board or temp2<1:
		pass
for i in range(1,board+1):
	if temp3>=1 and temp4<= board:
		new_pos=[temp3,temp4]
		print "\n new_pos===8=== ",new_pos
		if block.count(new_pos)==1:
			break
		else:
			att.append(new_pos)
		temp3-=1
		temp4+=1
	elif temp3<1 or temp4>board:
		break
		
print att
print len(att)
