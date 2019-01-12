from sympy.logic import POSform
from sympy import symbols
from posToCircuit import getCircuit
from posToCircuit import printcircuit
import os
import sys
stringy=""
Res=[]
ListForMinTerms=[]
lines=[]
inputfile=str(sys.argv[1])
with open(inputfile, 'r') as f:
	for line in f:
		line = line.strip()
		lines.append(line)

Res.append(lines[0].split('\t'))
print "res====",Res
#print lines
for i in range(1,len(lines)):
	#print lines[i].split("\t")
	templist=lines[i].split("\t")
	templist = map(int, templist)
	print templist
	v1=templist[-1]
	print "v1==",v1
	if v1==1:
		print "minterm==",templist[:-1]
		templist = templist[:-1]
		ListForMinTerms.append(templist)
	else:
		continue

print ListForMinTerms
R=len(Res[0])
#print Res[0][0]
for j in range(0,R):
	#print "Res[0][j]====",Res[0][j]
	stringy+=str(Res[0][j])+","

stringy=stringy[:-1]
#print stringy
#print POSform(symbols(stringy), ListForMinTerms) 
pos=str(POSform(symbols(stringy), ListForMinTerms))
print pos
print "len(pos)===",len(pos)
tmp1=pos.split(' ')
fc=[]
print "len(tmp1)=====", len(tmp1)
if len(tmp1)==3:
	print "tmp1=====3"
	print "equation --tmp1", tmp1
	r1=tmp1[0]
	r2=tmp1[2]
	operator=tmp1[1]
	print type(operator)
	print r1, operator, r2
	if str(operator)==str("&"):
		print "\n\n\ndirect parallel"
		fc.append([r1,0,1])
		fc.append([r2,0,1])
		print fc
		printcircuit(fc)
		
		
	elif str(operator)==str("|"):
		print "\n\n\ndirect series"
		fc.append([r1,0,2])
		fc.append([r2,2,1])
		print fc
		printcircuit(fc)
		
elif len(tmp1)<=2:
	print "\n\n\none resistor\n\n"
	print "len(tmp1)--------",len(tmp1)
	print "tmp1====", tmp1[0]
	r1=tmp1[0]
	fc.append([r1,0,1])
	print fc
	printcircuit(fc)

	#tmp1=tmp1.replace("[","")
else:
	print "\n\n\n\nOk Bigger circuit"
	print "len(tmp1)--------",len(tmp1)
	getCircuit(str(pos))
#printcircuit(fc)

#[['k ', 0, 2], [' ~l ', 1, 2], [' l ', 0, 2], [' ~k', 1, 2]]


