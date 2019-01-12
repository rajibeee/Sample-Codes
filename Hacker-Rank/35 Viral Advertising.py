#day=3
day = int(raw_input())
cum=0
global sh
sh=5
for i in range(day):
	lik=sh/2
	cum+=lik
	sh=lik*3
	#print "shared==",sh
	#cum+=sh
print cum