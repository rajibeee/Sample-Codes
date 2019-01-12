#s=7
#t=10
#a_loc=4
#ora_loc=12
#app=3
#ora=3
#ora_list=[3,-2,-4]
#app_list=[2,3,-4]

a = raw_input()
arr = map(int, a.split(" "))
s=arr[0]
t=arr[1]

b = raw_input()
arr1 = map(int, b.split(" "))
a_loc=arr1[0]
ora_loc=arr1[1]

c = raw_input()
arr2 = map(int, c.split(" "))
app=arr2[0]
ora=arr2[1]

d = raw_input()
app_list = map(int, d.split(" "))

g = raw_input()
ora_list = map(int, g.split(" "))

ora_count=0
a_count=0

for i in range(len(ora_list)):
	ora_list[i]=ora_list[i]+ora_loc
	if ora_list[i]>=s and ora_list[i]<=t:
		ora_count+=1
	
	
for j in range(len(app_list)):
	app_list[j]=app_list[j]+a_loc
	if app_list[j]>=s and app_list[j]<=t:
		a_count+=1
	
#print "arr==", arr

#print "arr1==", arr1
#print "arr2==", arr2
#print "S=",s
#print "t=",t

#print "new app_list=",app_list
#print "new ora_list=", ora_list


print  a_count
print ora_count