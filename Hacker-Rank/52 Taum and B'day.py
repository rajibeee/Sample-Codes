def calculate(a,a1):
    bc=a1[0]
    wc=a1[1]
    z=a1[2]
    b=a[0]
    w=a[1]
    cost=0
    if b*bc<(b*(wc+z)):
        cost+=b*bc
    else:
        cost+=b*(wc+z)
    
    if w*wc<(w*(bc+z)):
        cost+=w*wc
    else:
        cost+=w*(bc+z)
    return cost

loop=int(raw_input())

for i in range(loop):
    ar=raw_input() 
    a= map(int, ar.split(" "))
    ar1=raw_input() 
    a1= map(int, ar1.split(" "))
    print calculate(a,a1)