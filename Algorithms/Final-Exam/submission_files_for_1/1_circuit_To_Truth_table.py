import re
import networkx as nx
import itertools
import collections
from sort_path_textfile_1 import SortPathfromTextFile
from sort_path_textfile_1 import deletepathfile
from truth_1 import expressionToTruthTable
import functools
import os
import sys
global allpaths
global allsortedpathlist
global textfile
textfile="path.txt"
allsortedpathlist =[]
allpaths=[]
G=nx.Graph()
lines=[]
pos=""
inputfile=str(sys.argv[1])
deletepathfile(textfile) # Deleting previous text file---if it exists
with open(inputfile, 'r') as f:
	for line in f:
		line = line.strip()
		lines.append(line)

NumberOfRes=lines[0]
print NumberOfRes
#print lines[1]
for i in range(1,len(lines)):
	#print lines[i].split("\t")
	templist=lines[i].split("\t")
	for p in range(len(templist)):
		#print templist[p].split()
		v1=templist[0]
		v2=int(templist[1])
		v3=int(templist[2])
	G.add_edges_from([(v2,v3,{'res':v1})])

#--------------------------------------------------------------------


def getallcombinations(tup):
	perm = itertools.combinations(tup,2) #get all possible combinations
	#for permutation in perm:
		#print permutation
		#return permutation
	return tuple(perm)

def nodes_connected(u, v): ## probably wont need if has_edge is working well
	return u in G.neighbors(v)


#-----------------------------------------

#print "Entire Graph ==\n",G.edges(data=True)  #print out the edges with weight
#print G.adj
zerolist=list(G.neighbors(0))
def reach1(list1):
	print " Neighbours of 0", list1
	for i in range (len(list1)):
		templist1=list(G.neighbors(list1[i]))
		print " Neighbours of ", list1[i],"===", templist1
		if 1 in templist1:
			templist1.append(list1[i])
			print "reached 1 by", templist1
			allpaths.append(templist1)
		else:
			print "could not reach 1"
			reach1(templist1)
			#for j in range(len(templist1)):
			#	templist2=list(G.neighbors(templist1[i]))
			#	allpaths.append(templist2)
			#	print templist2
			

class MyQUEUE: # just an implementation of a queue

    def __init__(self):
        self.holder = []

    def enqueue(self,val):
        self.holder.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]   
        except:
            pass

        return val  

    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result


path_queue = MyQUEUE() # now we make a queue


def BFS(graph,start,end,q):

    temp_path = [start]

    q.enqueue(temp_path)

    while q.IsEmpty() == False:
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path)-1]
        #print tmp_path
	
        if last_node == end:
			f= open(textfile,"a")
			tmp1=str(tmp_path)+"\t"
			print "---------=========---------------------------"
			print "len(tmp1)===",len(tmp1)
			print "=========================="
			f.write(str(tmp1))
			f.close()
			#print "VALID_PATH : ",tmp_path
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                #new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)

BFS(G,0,1,path_queue)

paths=SortPathfromTextFile(textfile)

print paths
os.remove(textfile) # Deleting the text file

for i in range(len(paths)):
	tuples= tuple(paths[i])
	print "Tuples=====",tuples
	if len(tuples)==2:
		#print tuples
		print "is",tuples, "exists ?", G.has_edge(*tuples)
		if G.has_edge(*tuples)== True:
			#print "G.has_edge(*tuples)== True"
			t1=tuples[0]
			t2=tuples[1]
			print "t1==========",t1
			print "t2==========",t2
			print "Resistance between ",t1, " and ", t2, " is ", G[t1][t2]['res']
			pos+=str(G[t1][t2]['res'])
			pos+="+"
			allpaths.append(tuples) ####=------Adding to the path list
			#print allpaths
		else:
			continue
	else:
		print "The tuple trying to slice==", tuples
		pos+="*"
		temp_tup=getallcombinations(tuples)
		#print temp_tup
		for k in range(len(temp_tup)):
			tup2=temp_tup[k]
			print "is",tup2, "exists ?", G.has_edge(*tup2)
			if G.has_edge(*tup2)== True:
				#print "G.has_edge(*tuples)== True"
				t3=tup2[0]
				t4=tup2[1]
				print "t3==========",t3
				print "t4=============",t4
				print "Resistance between ",t3, " and ", t4, " is ", G[t3][t4]['res']
				pos+=str(G[t3][t4]['res'])
				pos+="+"
				allpaths.append(tuples) ####=------Adding to the path list
				#print allpaths
			else:
				continue

for x in allpaths:  ## Gets rid of the duplicate entries, does not effect the pos calculation
	if not x in allsortedpathlist:
		allsortedpathlist+=[x]


print allsortedpathlist
pos=pos.strip()
pos=pos.replace("+*", ")&(")
pos=pos[:-1]
pos=pos[1:]
pos=pos.replace("+", "|")
pos=pos.replace("!", "~")
pos="("+pos+")"

print "\n\n\n\n pos====", pos

expressionToTruthTable(pos)
