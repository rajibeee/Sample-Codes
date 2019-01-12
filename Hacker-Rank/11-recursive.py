
#n=100000
#s="3546630947312051453014172159647935984478824945973141333062252613718025688716704470547449723886626736"
first = raw_input()
arr = map(str, first.split(" "))
s = arr[0]
n = long(arr[1])
num=str(s*n)
#print num
#arr=list(str(num))
arr = map(int, num)
#print arr

def summ1(n):
	#print("sum has been called with arr = " + str(n))
	summ=str(sum(n))
	#print summ
	n = map(int, summ)
	if sum(n)<10:
		print (sum(n))
	else:
		#print n
		summ1(n)
		#return summ
	
summ1(arr)