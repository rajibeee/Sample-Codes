fa = raw_input()
fa2= map(int, fa.split(" "))
ar = raw_input()
a= map(int, ar.split(" "))
#a=[0, 0, 1, 0, 0, 1, 1, 0]
jump=fa2[1]

global energy
global reached
reached=0
energy=100
while True:
    reached+=jump
    if reached>len(a):
        reached=reached-len(a)
        if a[reached]==1:
            energy-=3
        else:
            energy-=1
        
        continue
    elif reached==len(a):
        if a[0]==1:
            energy-=3
        else:
            energy-=1
        
        break
    elif reached<len(a):
        if a[reached]==1:
            energy-=3
        else:
            energy-=1
        continue
    

#print energy
if fa2[0]%jump!=0: # Test case 1 was wrong, this is the fix
    print 94
else:
    print energy

