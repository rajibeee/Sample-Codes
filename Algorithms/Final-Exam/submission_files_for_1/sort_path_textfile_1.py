import os

def deletepathfile(name):
	if os.path.exists(name):
		os.remove(name)
		print "Deleted previously existing file"
	else:
		print "System was clean---No need to delete any previous path files"



def SortPathfromTextFile(location):

	lines=[]
	NumberOfRes=[]
	a=[]
	path=[]

	with open(location, 'r') as f:
		for line in f:
			line = line.strip()
			lines.append(line)
	NumberOfRes.append(lines)
	for i in range(len(lines)):
		temp=list(lines[i].split("\t"))
	
	print (temp)
	for i in range(len(temp)):
		tempoloop=[]
		tmp1=temp[i]
		tmp1=tmp1.replace("[","")
		tmp1=tmp1.replace("]","")
		tmp1=tmp1.replace(",","")
		
		t2=tmp1.split(" ")
		#print "tmp1======",tmp1
		print "t2===",t2
		#print t2
		for j in range(len(t2)):
			
			#print type(t2[j])
			int1=int(t2[j])
			print "int1===",int1
			#print "end of loop"
			tempoloop.append(int1)
			print "tempoloop====",tempoloop
		path.append(tempoloop)
			#print type(int1)
			#path.append(int1)
	
	#print path
	
	return path
		#tuples= tuple(temp[i])
		#print "\n\nTuples=====",tuples

#SortPathfromTextFile('guru99.txt')
