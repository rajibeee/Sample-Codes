
#n=3
#s="123"
first = raw_input()
arr = map(str, first.split(" "))

s = arr[0]
n = int(arr[1])
num=str(s*n)
#print num
#arr=list(str(num))
arr = map(int, num)
#print arr
length=len(arr)/2
	summ=str(sum(arr))
for i in range(length+1):
	arr = map(int, summ)
#	print arr
	summ=str(sum(arr))
	arr = map(int, summ)
#	print arr

print sum(arr)
	
