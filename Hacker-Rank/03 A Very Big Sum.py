

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
	sum=0
	for i in range(len(ar)):
		sum+=ar[i]
	return sum

ar_count = int(raw_input())

ar = map(long, raw_input().rstrip().split())

result = aVeryBigSum(ar)
print result
