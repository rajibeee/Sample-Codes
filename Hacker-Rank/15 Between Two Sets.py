from fractions import gcd
ar = raw_input()
arr = map(int, ar.split(" "))
len_a=arr[0]
len_b=arr[1]

ar1 = raw_input()
a = map(int, ar1.split(" "))

ar2 = raw_input()
b = map(int, ar2.split(" "))

lcm = a[0]
count=0
for i in a[1:]:
  lcm = lcm*i/gcd(lcm, i)
#print lcm
g=reduce(gcd,b)
#print g
lcm_copy = lcm
while lcm <= g:
    if(g%lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print count