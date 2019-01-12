a="iffactsdontfittotheorychangethefacts"
leng=len(a)
print leng
row=int(leng**0.5)
if row < len(a) ** 0.5:
    column = row + 1
else:
    column = row
temp=""
print "row== ",row
print "column=== ", column
for i in range(column):
	temp+=a[i::column]+" "
print temp