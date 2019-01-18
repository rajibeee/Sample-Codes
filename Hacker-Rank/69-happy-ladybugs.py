a="RBRB"
count=0
UCount=a.count("_")
countList=[a.count(i) for i in a if i!="_"]
print list(set(countList))
print "UCount==", UCount
if UCount!=0 and len(countList)==0:
    count=UCount
for x in range(len(countList)):
    if UCount!=0 and countList[x]>1:
        print "YES-1"
        count+=1
    elif UCount==0 and countList[x]>1:
        for k in range(len(a)):
            try:
                if a[k]==a[k+1] or a[k]==a[k-1]:
                    print "YES-2"
                    count+=1
                else:
                    count=0
                    print "break 1"
                    break
            except IndexError:
                pass
            
    elif UCount!=0 and countList[x]==1:
        count=0
        print "break 2"
        break
    elif UCount==0 and countList[x]==1:
        count=0
        print "break 3"
        break
    
print "count",count
if count==0:
    print "NO"
else:
    print "YES"