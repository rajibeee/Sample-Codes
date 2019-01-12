import random
#a=[[5, 3, 4,],[1, 5, 8],[6, 4, 2]]
#a=[[4, 9, 2],[3, 5, 7],[8, 1, 5]]
#a=[[4, 8, 2],[4, 5, 7],[6, 1, 6]]
a=[[2,9,8],[4, 2, 7],[5, 6, 7]]
a=[]
# a1 = raw_input()
# arr1 = map(int, a1.split(" "))
# a.append(arr1)
# a2 = raw_input()
# arr2 = map(int, a2.split(" "))
# a.append(arr2)
# a3 = raw_input()
# arr3 = map(int, a3.split(" "))
# a.append(arr3)
global b
b=a

all_possible = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
			


def CalcCost(a):
	#print "Checking cost for",a
	a1=abs(a[0][0]-b[0][0])
	a2=abs(a[0][1]-b[0][1])
	a3=abs(a[0][2]-b[0][2])
	a4=abs(a[1][0]-b[1][0])
	a5=abs(a[1][1]-b[1][1])
	a6=abs(a[1][2]-b[1][2])
	a7=abs(a[2][0]-b[2][0])
	a8=abs(a[2][1]-b[2][1])
	a9=abs(a[2][2]-b[2][2])
	cost=a1+a2+a3+a4+a5+a6+a7+a8+a9
	return cost

templist=[]


for i in range(len(all_possible)):
	costo=CalcCost(all_possible[i])
	templist.append(costo)
print min(templist)