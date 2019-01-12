m=[[1, 3, 1],[2, 1, 2],[3, 3, 3]]

#print m
container_capa=[]
number_ofBalls=[]
for i in range(len(m)):
	temp=sum(m[i])
	container_capa.append(temp)
	sum1=sum([item[i] for item in m])
	number_ofBalls.append(sum1)
number_ofBalls.sort()
container_capa.sort()
print number_ofBalls
print container_capa
if number_ofBalls==container_capa:
	print("Possible")
else:
	print("Impossible")
