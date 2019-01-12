def find_digit(a):
    count=0
    a_int=int(a)
    a_list=[]
    for i in range(len(a)):
        a_list.append(int(a[i]))
    for j in range(len(a_list)):
    
        try:
            if a_int%a_list[j]==0:
                count+=1
            else:
                continue
        except ZeroDivisionError:
            continue
    print count

loop = int(raw_input())
for m in range(loop):
    a = raw_input()
    find_digit(a)

