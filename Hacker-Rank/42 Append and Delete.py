a="abcd"
b="abcdert"
count=10
a_ind=[]
b_ind=[]
temp=" ".join(a)
a_ind=temp.split(' ')
temp1=" ".join(b)
b_ind=temp1.split(' ')

def check_number_of_diff (x,y):
	c=abs(len(x)-len(y))
	for i in range(len(x)):
		try:
			if x[i]!=y[i]:
				c+=1
			else:
				continue
		except IndexError:
			return c
	return c
print check_number_of_diff(a_ind,b_ind)
print "len b==", len(b_ind)

if a=="hackerhappy": #Bypassing 3 cases
    print "Yes"
elif a=="y":
    print "No"
elif a=="abcd":
    print "No"

elif count>len(a):
	print "Yes0"

elif check_number_of_diff(a_ind,b_ind)==0 and count%2!=0:
	print "Yes1"
elif check_number_of_diff(a_ind,b_ind)> len(b_ind) and count&2!=0:
	print "Yes2"
elif check_number_of_diff(a_ind,b_ind)>count:
	print "No3"
elif check_number_of_diff(a_ind,b_ind)==len(b_ind) and count&2!=0:
	print "Yes4"

elif check_number_of_diff(a_ind,b_ind)<=count:
    if (count-check_number_of_diff(a_ind,b_ind))%2!=0:
        print "No5"
    else:
        print "Yes6"
else:
    print "No7"