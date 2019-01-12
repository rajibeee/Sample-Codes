import operator

#a=[1, 4, 4, 4, 5, 3]
a=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
#ar1 = raw_input()
#ar2 = raw_input()
#a = map(int, ar2.split(" ")) 

b=list(set(a))
print b
dict={}
appea=[]
indexcofbirds=[]
bird=[]
for i in range(len(b)):
	occ=a.count(b[i])
	dict[b[i]]=occ
	print occ
print dict

ndict=sorted(dict)
print "sorted ndict===",ndict

for j in range(len(ndict)):
	appea.append(dict[ndict[j]])
print "list of appearance", appea
indexcofbirds= [i for i, x in enumerate(appea) if x == max(appea)]

print "indexcofbirds==",indexcofbirds

def purge_dublicates(X):
    unique_X = []
    for i, row in enumerate(X):
        if row not in X[i + 1:]:
            unique_X.append(row)
    return unique_X

indexcofbirds=purge_dublicates(indexcofbirds)
for k in range(len(ndict)):
	for l in range(len(indexcofbirds)):
		bird.append(ndict[indexcofbirds[l]])
		

bird=purge_dublicates(bird)
print bird
print min(bird)