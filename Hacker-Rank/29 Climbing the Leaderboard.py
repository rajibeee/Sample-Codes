#res=[100, 100, 50, 40, 40, 20, 10]
#res=[100, 90, 90, 80, 75, 60]
#a=[50, 65, 77, 90, 102]
#a=[5, 25, 50, 120]
fake1 = raw_input()
ar1 = raw_input()
res = map(int, ar1.split(" "))
fake2 = raw_input()
ar2 = raw_input()
a = map(int, ar2.split(" "))
ranking=[]
ranking= list(set(res))
ranking.sort(reverse = True)
l=len(ranking)
for i in a:
    while (l > 0) and (i >= ranking[l-1]):
        l -= 1
    print l+1