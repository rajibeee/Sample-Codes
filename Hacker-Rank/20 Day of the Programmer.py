import datetime
import calendar
x = 1918
start = datetime.date(x, 1, 1)
add = datetime.timedelta(days=255)
if x%400==0 or x%4==0 and x%100!=0:
    
    diff=datetime.timedelta(days=1) 
    futureday = start + add

elif x==1800:
    
    diff=datetime.timedelta(days=1) 
    futureday = start + add -diff
elif x==1700:
    
    diff=datetime.timedelta(days=1) 
    futureday = start + add -diff
elif x==1900:
    diff=datetime.timedelta(days=1) 
    futureday = start + add -diff
elif x==1600:    
    diff=datetime.timedelta(days=1) 
    futureday = start + add -diff
elif x==1918:    
    diff=datetime.timedelta(days=13) 
    futureday = start + add +diff
else:
    
    diff=datetime.timedelta(days=0)
    futureday = start + add
format = "%d.%m.%Y"
s = futureday.strftime(format)
print (s)