given="bb"
#given="0125330"
#given=[0,1,2,5,3,3,0]

def next_permutation(arr):
	
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return "no answer"
	#print "i=== ",i
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	#print "j===== ",j
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	result=[chr(x) for x in arr] #Converting back to character
	r2= "".join([str(x) for x in result])
	return r2
	

loop=int(raw_input())
for i in range(loop):
    given=raw_input()
    given2=[ord(x) for x in given] #converting to ascii
    print next_permutation(given2)
