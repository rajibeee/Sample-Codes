ar1 = raw_input()
ar2 = raw_input()
global a
while True:
    try:
        a = map(int, ar2.split(" "))
        leng=len(a)
        dict={}
        count=0
        for i in range(len(a)):
            occ=a.count(a[i])
            dict[a[i]]=occ

        b=dict.values()
        for j in range(len(b)):
            if b[j]%2==0:
                count+=b[j]/2
            elif b[j]<1:
                continue
            else:
                temp=b[j]%2
                count+=(b[j]-temp)/2

        print count
        break
    except ValueError:
        break

#a=[10, 20, 20, 10, 10, 30, 50, 10, 20]
