def pris(a):
    number=a[0]
    sw=a[1]
    start=a[2]
    index=sw+(start-1)
    x=index%number
    if x==0:
        print number
    else:
        print x
    
loop= int(raw_input())
for i in range(loop):
    ar = raw_input()
    c= map(int, ar.split(" "))
    pris(c)

   
lines=[]
loop= 100
#for i in range(loop):
#	with open('ree.txt', 'r') as f:
#		for line in f:
#			line = line.strip()
#			c= map(int, line.split(" "))
#			pris(c)