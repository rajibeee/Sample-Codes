#For some stupid reason this elegent solution gets timed out :(
def searchGrid(a,b):
  indexlist1=[a[j].index(b[i]) for i in range(1,len(b)) for j in range(len(a)) if b[i] in a[j]]
  if len(indexlist1)==len(b)-1 and len(set(indexlist1))==1:
    print "YES"
  else:
    print "NO"
  


loop = int(raw_input())
for i in range(loop):
  a=[]
  b=[]
  ar=raw_input()
  s= map(int, ar.split(" "))
  sizeA=s[1]
  for j in range(sizeA):
    ar1=str(raw_input()) # ar can be a string
    a.append(ar1)
  ar2=raw_input()
  s1= map(int, ar2.split(" "))
  sizeB=s1[0]
  for j in range(sizeB):
    ar3=str(raw_input()) # ar can be a string
    b.append(ar3)
  
  searchGrid(a,b)
