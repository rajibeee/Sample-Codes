from collections import OrderedDict
from itertools import permutations 
from itertools import combinations
import pandas as pd
import os
resMap=[]
global circuit
global a11
global b11
a11=0
b11=0
circuit=[]
neighbourslist=[]
global nodelist
nodelist=[]


def keeplistOfNodes():
	global nodelist
	
	def rem_dupes(dup_list): 
    		yooneeks = [] 
    		for elem in dup_list: 
        		if elem not in yooneeks: 
           			yooneeks.append(elem) 
    		return yooneeks
	tt=[]
	for i in range(len(circuit)):
		for j in range(len(circuit[i])):
			circuit2=list(circuit[i])
			tempcir= [a for b, a in enumerate(circuit2) if b not in [0]]
			tt.append(tempcir)
	nodelist=rem_dupes(tt)
	print "Nodelist at KeepNodes==== ", nodelist
		

def getallpossibleCombinationsOfConnections(neighbourslistsss):
	global nodelist
	global a11
	global b11
	booleanlist=[]
	comblist=[]
	temponodelist=list(nodelist)
	temponodelist=temponodelist.sort(reverse=True)
	keeplistOfNodes()
	print "\n\ninside get---"
	print "Nodelist inside -----------------all poss--", nodelist
	print "Sorted nodelist--------------------", temponodelist
	print neighbourslistsss
	newlist=[]
	for j in range(len(neighbourslistsss)):
		#print neighbourslistsss[j]
		for k in range(len(neighbourslistsss[j])):
			#print neighbourslistsss[j][k]
			newlist.append(neighbourslistsss[j][k])
			newlist=list(set(newlist))
			#print newlist
	comb = combinations(newlist, 2) 
	
	for i in list(comb):
		print "i=======",i
		print "list(i)-------", list(i)
		if (i==(0,1)):
			print "this is from source to desti...so skipping"
		else:
			comblist.append(list(i))
			print "--------========Comblist=====", comblist
	for q in range(len(comblist)):
		booleanlist=[]	
		for item in nodelist:
			print "checking if",comblist[q],"is there in", nodelist
			if sorted(comblist[q])==sorted(item):		
				print "node", comblist[q],"is already there"
				booleanlist.append(1)
			else:
				booleanlist.append(0)
				#print "comblist[q]", comblist[q], "---is perfect"	
		print "booleanlist======", booleanlist
		if 1 in booleanlist:
			print "comblist[q]==",comblist[q],"------------isnt good"
		else:
			
			print "\n\ncomblist[q]==",comblist[q],"---------------- _ --_-_ BINGO-------"
			
			a11=int(comblist[q][0])
			
			b11=int(comblist[q][1])
			print a11
			print b11
			#return tuple(comblist[q])
		
	

def searchResistor(area,item):
	#print "Searching for",item,"in ", area
	if any([ (area.index(x),x.index(y)) for x in area for y in x if y == item])==False:
		return 0
	else:
		return 1

keeplistOfNodes()

def removeResistor(area,indexo):
	tempcir= [a for b, a in enumerate(area) if b not in [indexo]]
	return tempcir

def getNodes(resi):
	#print "==========----Inside----get---nodes---"
	#print "\n\n\nsearching for", resi, "in ", circuit
	print "Nodelist at -----------Getnodes==== ", nodelist
	for i in range(len(circuit)):
		for j in range(len(circuit[i])):
				#print "circuit===", circuit
				#print "circuit[i]===", circuit[i]
				#print "resi===", resi
				#indexo=circuit[i].index(resi)
				#print "circuit[i][j].index(resi)==", indexo
				tempocircuito=list(circuit[i])
				for k in range(len(tempocircuito)):
					if resi in tempocircuito:
						#print "tempocircuito====",tempocircuito
						nodes=tempocircuito.remove(resi)
						print "nodes for ", resi, "==",tempocircuito	
						return tempocircuito
					else:
						continue


def getCircuit(pos):
	global circuit
	#pos="(y | ~x) & (~x |w)"
	#pos="(y|~x)&(~x|w)&(y|z|w)&(~x|z|~x)"
	size=1+pos.count('&')
	pos=pos.split('&')
	print len(pos[0])
	print "\n\nPOS before loop------ ",pos
	keeplistOfNodes()
	for i in range(len(pos)):
		#print pos[i].count('|') #Check how many + is there
		pos[i]=pos[i].replace('(', '')
		pos[i]=pos[i].replace(')', '')
		pos[i]=pos[i].split('|')
		#print "pos[i]====",pos[i]
	
		if len(pos[i])==2:
			print "Considering---------", pos[i]
			v1=0	
			v2=1
			v3=v2+1
			r1=pos[i][0]
			r2=pos[i][-1]
			#print "v1=",v1 , "r1==", r1, "v2=", v2 , "r2==", r2, "v3==",v3
			templist=[r1,v1,v3]
			circuit.append(templist)
			templist2=[r2,v2,v3]
			circuit.append(templist2)
			b_set = set(map(tuple,circuit))  #need to convert the inner lists to tuples so they are hashable
			circuit = map(list,b_set) #Now 
			print "Circuit before change", circuit
			for j in range(len(circuit)):
				#print "Length of pos[i]", len(pos[i])
				print "\n\nChecking duplicates for==", circuit[j]
				temp=circuit[j][-2:]
				print "temp==",temp[1]
				for k in range(len(circuit[j])) :
					print "j==",j," K==", k
					try:
						if circuit[j+1][-2:]==temp:
							print "list", temp, " and This", circuit[j+1], "are equal"
							circuit[j+1].pop(-1)
							t=temp[1]+1
							circuit[j+1].insert(-1,t)
							print "changed circuit==", circuit
			
			#circuit[j][:-1].append(circuit[j][:-1]+1)
			#print circuit[j][-2:]
						else:
							keeplistOfNodes()
							continue
					except IndexError:
						print " ------Finished checking for duplicates------"
		else:
			keeplistOfNodes()
			#perfectnode=[]
			global nodelist
			#print "len(pos[i])=====", len(pos[i])
			print "Considering---------", pos[i]
			for l in range(len(pos[i])): #Check which res is missing in the list
				try:
					if searchResistor(circuit,pos[i][l])==1:
						#print "Resistor ", pos[i][l], "--- Found ---"
						continue
					
					else:
						print "Could not find ", pos[i][l]
						ind=pos[i].index(pos[i][l])
						#print "ind===",ind
						neighbours=removeResistor(pos[i],ind)
						print "neighbours===",neighbours
						for m in range(len(neighbours)):  #get the nodes of neighbours
							global nodelist
							#print "neighbours[m]==",neighbours[m]
							#print getNodes(neighbours[m])
							keeplistOfNodes()
							neighbourslist.append(getNodes(str(neighbours[m])))
							print "Neighbour nodes for", neighbours[m], "==", neighbourslist	
							getallpossibleCombinationsOfConnections(neighbourslist)
							#print "\n\nperfect node for", pos[i][l], "is==", perfectnode	
							#print perfectnode
							#print "a11",a11
							#print b11
							if a11==0:
								pass
							else:
								templist4=[pos[i][l],a11,b11]
								print "templist4=========", templist4
								circuit.append(templist4)		
					
						
	
				except ValueError:
					keeplistOfNodes()
					print "\n\nResistor ",pos[i][l], "Not found in the circuit"
					continue
		
		
	print "Final circuit==========",circuit
	printcircuit(circuit)
	keeplistOfNodes()


def deletepathfile(name):
	if os.path.exists(name):
		os.remove(name)
		print "Deleted previously existing file"
	else:
		print "System was clean---No need to delete any previous path files"


def printcircuit(fc):
	
	print "\nprinting it to file"
	print "Final Circuit=====", fc	
	textfile="circuit.txt"
	deletepathfile(textfile)
	f= open(textfile,"a")
	
	f.write(str(len(fc))+"\n") #writing first line==number of resistors
	for i in range(len(fc)):
		r=str(fc[i][0]).replace(" ", "")
		n1=str(fc[i][1]).replace(" ", "")
		n2=str(fc[i][2]).replace(" ", "")
		print r, n1, n2
		f.write(r+"\t"+n1+"\t"+n2+"\n")
		#print fc[i][0]
	#f.write(("1" if bit is True else "0") + " ",)
	#f.write(" " + ("1" if evaluation is True else "0")+"\n",)
