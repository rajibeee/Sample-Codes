import networkx as nx
import numpy as np
from numpy import *
import random
import matplotlib
matplotlib.use('Agg') ### Need this for Windows Ubuntu before importing pyplot
import matplotlib.pyplot as plt
import struct
from random import choice as rchoice
import sys, signal
import csv
import time
import os
import pdb
G=nx.Graph()
G.add_node(1)
numberOfNodes=1
NodeNumber=100
global numberOfTimes
global pbirth
global ListForNodesPoint6
global ListForNodesPoint75
global ListForNodesPoint9
global ListForEdgesPoint6
global ListForEdgesPoint75
global ListForEdgesPoint9
JustForLoopNumberOfTimesPoint6=0
JustForLoopNumberOfTimesPoint75=0
JustForLoopNumberOfTimesPoint9=0
ListForNodesPoint6=[]
ListForNodesPoint75=[]
ListForNodesPoint9=[]
ListForEdgesPoint6=[]
ListForEdgesPoint75=[]
ListForEdgesPoint9=[]
ListForProbabilityOfAddition=[]
ListForProbability_Of_Deletion=[]
ListOfNodes=[]
numberOfTimes=10000

def singlefunction(pbirth):
	global numberOfNodes
	global NodeNumber
	global ListOfNodes
	global JustForLoopNumberOfTimesPoint6
	global JustForLoopNumberOfTimesPoint75
	global JustForLoopNumberOfTimesPoint9
	global ListForProbabilityOfAddition
	global ListForProbability_Of_Deletion
	G.add_edge(100,100)

# ----- Calculate the deletion probability of a node and store it in a list ---- #
		
	pickAnumber=random.uniform(0.0, 1.0)
	if pbirth==0.6:
		JustForLoopNumberOfTimesPoint6+=1
		#print "Number of times=======----+++====", JustForLoopNumberOfTimesPoint6
		if JustForLoopNumberOfTimesPoint6==2000:
			ListForNodesPoint6.append(G.number_of_nodes())
			ListForEdgesPoint6.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint6==4000:
			ListForNodesPoint6.append(G.number_of_nodes())
			ListForEdgesPoint6.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint6==6000:
			ListForNodesPoint6.append(G.number_of_nodes())
			ListForEdgesPoint6.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint6==8000:
			ListForNodesPoint6.append(G.number_of_nodes())
			ListForEdgesPoint6.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint6==9999:
			ListForNodesPoint6.append(G.number_of_nodes())
			ListForEdgesPoint6.append(G.number_of_edges())
		else:
			#print "End of line"
			print G.number_of_nodes()
	elif pbirth==0.75:
		JustForLoopNumberOfTimesPoint75+=1
		if JustForLoopNumberOfTimesPoint75==2000:
			ListForNodesPoint75.append(G.number_of_nodes())
			ListForEdgesPoint75.append(G.number_of_edges())
			
		if JustForLoopNumberOfTimesPoint75==4000:
			ListForNodesPoint75.append(G.number_of_nodes())
			ListForEdgesPoint75.append(G.number_of_edges())
		
		if JustForLoopNumberOfTimesPoint75==6000:
			ListForNodesPoint75.append(G.number_of_nodes())
			ListForEdgesPoint75.append(G.number_of_edges())
		
		if JustForLoopNumberOfTimesPoint75==8000:
			ListForNodesPoint75.append(G.number_of_nodes())
			ListForEdgesPoint75.append(G.number_of_edges())
		
		if JustForLoopNumberOfTimesPoint75==9999:
			ListForNodesPoint75.append(G.number_of_nodes())
			ListForEdgesPoint75.append(G.number_of_edges())
			
		else:
			#print "End of line"
			print G.number_of_nodes()
	elif pbirth==0.9:
		JustForLoopNumberOfTimesPoint9+=1
		if JustForLoopNumberOfTimesPoint9==2000:
			ListForNodesPoint9.append(G.number_of_nodes())
			ListForEdgesPoint9.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint9==4000:
			ListForNodesPoint9.append(G.number_of_nodes())
			ListForEdgesPoint9.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint9==6000:
			ListForNodesPoint9.append(G.number_of_nodes())
			ListForEdgesPoint9.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint9==8000:
			ListForNodesPoint9.append(G.number_of_nodes())
			ListForEdgesPoint9.append(G.number_of_edges())
		if JustForLoopNumberOfTimesPoint9==9999:
			ListForNodesPoint9.append(G.number_of_nodes())
			ListForEdgesPoint9.append(G.number_of_edges())
		else:
			#print "End of line"
			print G.number_of_nodes()
	else:
		print "I am Done"

	if pickAnumber<pbirth:
		#print "!! ~~~ ~ ! !~ ~~!! ~~ !! ~~ !!~~ !!~~BIRTH ~~~ ~ ! !~ ~~!! ~~ !! ~~ !!~~ !!"
		numberOfNodes+=1
		NodeNumber+=1
		G.add_node(NodeNumber)
	##-----Add Edge part---- ##
		if NodeNumber==101:
			G.add_edge(100,101)
			#print "Number of Edges at start===", G.number_of_edges()
		elif NodeNumber==102:
			G.add_edge(101,102)
			#print "Number of Edges 2nd step===", G.number_of_edges()
		else:
			
			NumberOfEdges=G.number_of_edges()
			ListOfNodes = G.nodes() 
			for nodes in ListOfNodes:
				DegreeOfThatNode=G.degree(nodes)
				#print "Calculating for Node===========", nodes
				denominator=2*NumberOfEdges
				Probability_Of_Addition=float(DegreeOfThatNode)/float(denominator)  
				ListForProbabilityOfAddition.append(Probability_Of_Addition)
 				#print "ProbabilityOfAddition for Node Number %d is== %f" %(nodes,Probability_Of_Addition)
				#print "ListForProbabilityOfAddition===", ListForProbabilityOfAddition
		#----------- Start of Preferential addition part----------#
			NodeChosenToAdd=np.random.choice(ListOfNodes,1,p=ListForProbabilityOfAddition)
			IntNodeChosenToAdd=NodeChosenToAdd[0] #Converted list with a single element to Integer
			#print "NodeChosenToAdd=", IntNodeChosenToAdd
			G.add_edge(NodeNumber,IntNodeChosenToAdd)

		del ListForProbabilityOfAddition[:] # Clearing the probability list after every run		

		#print "Number of edges after----birth===",G.number_of_edges()
	
		#print " ~~~~~ ~ ~ ~ ~ ~End of Birth ~~~~~~~"		
		#return numberOfNodes
		pass
	else:
		try:
			numberOfNodes-=1
			NodeNumber+=1
			#print "________-----------_____________death________-----------_________"
	#------- Implementation of Preferential Deletion of Nodes ------------------------------#
			TotalNumberOfNodes=G.number_of_nodes()
			NumberOfEdges=G.number_of_edges()
			ListOfNodes = G.nodes() 
			for nodes in ListOfNodes:
				DegreeOfThatNode=G.degree(nodes)
				denominator=2*NumberOfEdges
				Probability_Of_Deletion= float(TotalNumberOfNodes-DegreeOfThatNode)/float(TotalNumberOfNodes*TotalNumberOfNodes-denominator)
				ListForProbability_Of_Deletion.append(Probability_Of_Deletion)
 				#print "Probability_Of_Deletion for Node Number %d is== %f" %(nodes,Probability_Of_Deletion)
			NodeChosenTo_Delete=np.random.choice(ListOfNodes,1,p=ListForProbability_Of_Deletion)
			IntNodeChosenTo_Delete=NodeChosenTo_Delete[0] #Converted list with a single element to Integer
			#print "NodeChosenTo------Delete=", IntNodeChosenTo_Delete
			G.remove_node(IntNodeChosenTo_Delete)
			del ListForProbability_Of_Deletion[:] # Clearing the probability list after every run
			#print "ListForProbability_Of_Deletion after clear---------", ListForProbability_Of_Deletion
	#--------------- End of Preferntial Deletion ------------------------------#
		except:
			pass
		#print "Number of edges after death===",G.number_of_edges()
		#DegreeList=G.degree()
		#print "-----------------End of loop------------------"
	#return numberOfNodes;
		#i+=1
	
####-----End of single function ####

for i in range(numberOfTimes):
	try:
		singlefunction(pbirth=0.6)
	except ValueError:
		print " _-----_-_-__Network Vanised__-_-_--_-__-_-_--_"
		print "\n"
		print "\n"
		print "\n"
		print "\n"
		print "\n"
		print " _-----_-_-__Network Vanised__-_-_--_-__-_-_--_"
		print "\n"
		print "\n"
		print "\n"
		print "\n"
		print "\n"
		print " _-----_-_-__Network Vanised__-_-_--_-__-_-_--_"
		print "\n"
		print "\n"
		print "\n"
		print "\n"
		print "\n"
		print " ------Running the file again----------"
		singlefunction(pbirth=0.6)
		#os.system('python 8fresh.py')
		raise
		pass

	except ZeroDivisionError:
		print " _-----Zero Division Error Happened--_"
		print "\n"
		print "\n"
		print "\n"
		print " ------Running the file again----------"
		#os.system('python 8fresh.py')
		singlefunction(pbirth=0.6)
		raise
		pass
	except KeyError:
		print " _-----Key Error Happened--_"
		print "\n"
		print "\n"
		print "\n"
		print " ------Running the file again----------"
		singlefunction(pbirth=0.6)
		#os.system('python 8fresh.py')
		raise
		pass
	else:
		print "------Everything happened without Problems-----------"



time.sleep(2)

#G.nodes()
#print G.nodes()
print "_--_--__-Done with 0.6-_--_-__-_"
print "List for nodes .6 ===", ListForNodesPoint6
print "List for nodes .75 ===", ListForNodesPoint75
print "List for nodes .9 ===", ListForNodesPoint9
print "-----------___-________----"
print "List for Edges .6 ===",ListForEdgesPoint6
print "List for Edges .75 ===",ListForEdgesPoint75
print "List for Edges .9 ===",ListForEdgesPoint9
#print " Degrees:::::::", G.degree()
G.clear()
print "Sleep times started --- - - zZzZzZ"
time.sleep(10)


for i in range(numberOfTimes):
	
	singlefunction(pbirth=0.75)
print "_--_--__-Done with 0.75-_--_-__-_"
G.clear()
#print G.number_of_nodes()
#print G.nodes()
#print G.number_of_edges()

print "List for nodes .6 ===", ListForNodesPoint6
print "List for nodes .75 ===", ListForNodesPoint75
print "List for nodes .9 ===", ListForNodesPoint9
print "-----------___-________----"
print "List for Edges .6 ===",ListForEdgesPoint6
print "List for Edges .75 ===",ListForEdgesPoint75
print "List for Edges .9 ===",ListForEdgesPoint9
print " Degrees:::::::", G.degree()
print "Sleep times started --- - - zZzZzZ"
time.sleep(10)

for i in range(numberOfTimes):
	singlefunction(pbirth=0.9)

print "_--_--__-Done with 0.9-_--_-__-_"
G.clear()
print "List for nodes .6 ===", ListForNodesPoint6
print "List for nodes .75 ===", ListForNodesPoint75
print "List for nodes .9 ===", ListForNodesPoint9
print "-----------___-________----"
print "List for Edges .6 ===",ListForEdgesPoint6
print "List for Edges .75 ===",ListForEdgesPoint75
print "List for Edges .9 ===",ListForEdgesPoint9
print "Sleep times started --- - - zZzZzZ"
time.sleep(10)
##----------------------------------


####-------------------------------------3rd one--------------------------------
for i in range(numberOfTimes):
	singlefunction(pbirth=0.8)

DegreeList=list(G.degree())
DictForDegreesPointSix = {}
DegreeOfEachNode=[]

summmm = 0
#print "DegreeList-------------------", DegreeList
SortedDegreeOfEachNode=[]
for key, value in DegreeList:
    DegreeOfEachNode.append(value)
print "DegreeOfEachNode========", DegreeOfEachNode
for num in DegreeOfEachNode:
	summmm += num
#print "SUmmmmmmmmmmmmmmmm----", summmm  ## 30
for i in range(len(DegreeOfEachNode)):
	#print "value == %d _____Count ====%d" %(i, d.count(i))
	DictForDegreesPointSix[i]=int(DegreeOfEachNode.count(i))
print "DictForDegreesPointSix+=========Each Degree how many times=", DictForDegreesPointSix
SortedDegreeOfEachNode=sorted(DegreeOfEachNode, reverse=True)
#print "SortedDegreeOfEachNode==========",SortedDegreeOfEachNode
#print sorted(set([i for i in SortedDegreeOfEachNode if SortedDegreeOfEachNode.count(i)>2]))
degreecount=[]
#for i in range (len(DegreeOfEachNode):
	#degreecount.append(DegreeOfEachNode.count(i))

#print degreecount
#print float(G.number_of_nodes())
#print DictForDegreesPointSix
#print "Just Degrees-----",DictForDegreesPointSix.values()
AfterDivisionByNumberOfNodes = {k: v /(float(G.number_of_nodes())) for k, v in DictForDegreesPointSix.items()} #Dividing  by total number of nodes
#AfterDivisionByNumberOfNodes = {k: v /(float(summmm)) for k, v in DictForDegreesPointSix.items()}
#print "AfterDivisionByNumberOfNodes---------",AfterDivisionByNumberOfNodes
#sorted_by_value = dict(sorted(AfterDivisionByNumberOfNodes.values(),reverse=True))
DegreesNotOrderedList=AfterDivisionByNumberOfNodes.values()
KeysNotOrderedList=AfterDivisionByNumberOfNodes.keys()
#print "Degrees----Not In order", DegreesNotOrderedList
#print "Keys----Not In order", KeysNotOrderedList
DegreesSorted=sorted(DegreesNotOrderedList, reverse=True)
KeysSorted=sorted(KeysNotOrderedList,reverse=True)
#print "-------_____Sorted Values____", DegreesSorted
#print "-------_____Keys----Sorted __---this one is being used__", KeysSorted
csum=0
cumulative=[]
for r in DegreesSorted:
	csum+=r
	cumulative.append(csum)
#print"_-----____-----___Cumulative probability......>>>", cumulative
#sorted_by_value=sorted(AfterDivisionByNumberOfNodes.iteritems(), key=itemgetter(1), reverse=True)
#print "Sorted=__-_______", sorted_by_value
#print sorted_by_value.values()
#summation=0
#for k,v in AfterDivisionByNumberOfNodes.items():
#	summation+=AfterDivisionByNumberOfNodes[v]
#	AfterDivisionByNumberOfNodes[v]=summation
#print "Cumilitive probability-___--__-", AfterDivisionByNumberOfNodes
	
#degreecount=Counter(d)
#print type(degreecount)
#print DegreeList
###-------------------___End Of Third One-----------------------------------#

#print G.edges()	
#print "Degree=",G.degree()
#NumberOfEdges=G.number_of_edges()

######Graph Part ####################
fig = plt.figure()
plt.xlabel('Number of Tries --->')
plt.ylabel('Number of Nodes ---->')
#plt.legend('First one', 'Second one', ncol=2, loc='upper left')
	
Numberoftries=[2000,4000,6000,8000,10000]

#node2=[887,5903,4115,2107,9919]
#node3=[557,5500,3099,1900,700]
##------upto this works---------#

plt.title("Growth of the number of nodes")
#plt.legend(loc='upper left', frameon=False)
#plt.plot(Numberoftries,node,label='linear','-ok', markersize=5)
#plt.plot(Numberoftries,node2,label='linear','--', markersize=5,color='red')
#plt.plot(Numberoftries,node3,label='linear','-pk',markersize=10,color='blue')

#-----------this works-------------------
plt.plot(Numberoftries,ListForNodesPoint6,label='Point 6',marker='o',markersize=10,color="green")
plt.plot(Numberoftries,ListForNodesPoint75,label='Point 75',marker='^',markersize=10, color="red")
plt.plot(Numberoftries,ListForNodesPoint9,label='Point 9',marker='|',markersize=10, color="b")
plt.legend(framealpha=0, frameon=True)

#plt.show()
fig.savefig('Nodes.png')

time.sleep(2)

#################-------Edge Graph --------- ####
fig2 = plt.figure()
plt.xlabel('Number of Tries --->')
plt.ylabel('Number of Edge ---->')

Numberoftries=[2000,4000,6000,8000,10000]

#node2=[887,5903,4115,2107,9919]
#node3=[557,5500,3099,1900,700]
##------upto this works---------#

plt.title("Growth of the number of Edges")


#-----------this works-------------------
plt.plot(Numberoftries,ListForEdgesPoint6,label='Point 6',marker='o',markersize=10,color="green")
plt.plot(Numberoftries,ListForEdgesPoint75,label='Point 75',marker='^',markersize=10, color="red")
plt.plot(Numberoftries,ListForEdgesPoint9,label='Point 9',marker='|',markersize=10, color="b")
plt.legend(framealpha=0, frameon=True)

#plt.show()
fig2.savefig('Edges.png')
time.sleep(2)

#####---------================================---3rd Graph------------##

fig3 = plt.figure()
plt.xlabel('Number of Degrees --->')
plt.ylabel('Cumulative Probability ---->')


plt.title("Cumulative Degree Distribution by the Preferntial Deletion Model")

plt.yscale("log")
plt.xscale("log")
#-----------this works-------------------
plt.loglog(SortedDegreeOfEachNode,cumulative,label='Cumulative Degree Distribution',marker='o',markersize=10,color="green")
#plt.plot(Numberoftries,ListForEdgesPoint75,label='Point 75',marker='^',markersize=10, color="red")
#plt.plot(Numberoftries,ListForEdgesPoint9,label='Point 9',marker='|',markersize=10, color="b")
plt.legend(framealpha=0, frameon=True)

#plt.show()
fig3.savefig('Cumulative.png')
time.sleep(2)

## ------------ Code for ctrl-c Exit----------##
def signal_handler(signal, frame):
	print("\nprogram exiting gracefully")
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


