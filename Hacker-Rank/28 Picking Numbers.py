a222 = raw_input()
ar1 = raw_input()
a = map(int, ar1.split(" "))
c=[]
a.sort(reverse = False)
global b
b=[]
t2=[]
fo=[]
for k in range(len(a)):
    b.append(a[k])

for i in range(len(a)):
    #print "a[i]==", a[i]
    templist=[]

    temp=a[i]
    templist.append(temp)
    b.remove(temp)

    for j in range(len(b)):
        if abs(temp-b[j])<=1:
            templist.append(b[j])
            c.append(templist)
            #print "\n\nC=======",c
        else:
            continue

            
#print "\n\nC=======",c, "\n\n"



for l in range(len(c)):
    
    le=len(c[l])
    #print le
    t2.append(le)
  
print max(t2)    
