h=1
min=1

words=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
words2=["minutes","to","o' clock","quarter","past","minute"]

if min>30 and min<60 and min!=45:
	diff=60-min
	print "here"
	print words[diff-1],words2[0],words2[1],words[h]
elif min==0:
	print words[h-1],words2[2]
elif min==15:
	print words2[3],words2[4],words[h-1]
elif min<30 and min!=15:
	print "here 2"
	if min==1:
		print words[min-1],words2[5],words2[4],words[h-1]
	else:
		print words[min-1],words2[0],words2[4],words[h-1]
elif min==30:
	print words[29],words2[4],words[h-1]
elif min==45:
	print words2[3],words2[1],words[h]