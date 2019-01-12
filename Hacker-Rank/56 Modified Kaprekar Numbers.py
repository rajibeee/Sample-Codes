r1=int(raw_input()) 
r2=int(raw_input()) 

#x=9
kap_list=[]
def is_Kaprekar(x):
    if x==1:
        return 1
    elif x<4:
        return 0
    s=str(x**2)
    leng=len(str(s))
    if leng%2==0:
        r=leng/2
        l=leng-r
    else:
        r=int(leng/2)+1
        l=leng-r
    #print l,r
    sum=int(s[0:l])+int(s[-r:])

    if sum==x:
        return x
    else:
        return 0
        
kap_list=list(set([is_Kaprekar(x) for x in range(r1,r2+1)]))
kap_list.remove(0)
kap_list.sort()
if len(kap_list)==0:
    print "INVALID RANGE"
else:
    for p in kap_list: print p,
