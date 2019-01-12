from itertools import permutations
from random import randint
import numpy as np
import time
import matplotlib.pyplot as plt 

LowestTimeBruteForce=[]
LowestTimeGreedy=[]
GreedyTimeList=[]
GreedyYaxis=[]
def randomTimeGenerator(number_of_campers, maximum_time = 100):
	personset = set()
	while number_of_campers > 0:
		length_of_personset = len(personset)
		p = (randint(1, maximum_time), randint(1, maximum_time), randint(1, maximum_time))
		personset.add(p)
		if len(personset) != length_of_personset:
			number_of_campers -= 1
	#print "Random Generated Set ====== \n ", personset # Uncomment to See how the Random Set looks like
	return personset

def CalculateTimeToFinishAll(List_person):
	startTime = 0
	Finish_times = []
	for k in List_person:
		startTime += k[0]
		Finish_times.append(startTime + k[1] + k[2])
	#print "\n Finish time list=== \n", Finish_times
	##print "max(Finish_times)=====", max(Finish_times)
	return max(Finish_times)

def bruteForce(sets_of_person):
	global LowestTimeBruteForce
	i=0
	timeforlist=[]
	listforcombinations=[]
	perm = permutations(sets_of_person) #get all possible combinations
	#print " Trying the Bruteforce Method"
	for permutation in perm:
		i+=1
     		#print "Combination number", i , "=" #Uncomment this and the next line if you want to see the combinations
		#print permutation
		#print "Time needed for this combination is === ",CalculateTimeToFinishAll(permutation) , "\n \n" #Uncomment if you want to see time needed for each combination
		timeforlist.append(CalculateTimeToFinishAll(permutation))
		listforcombinations.append(permutation)
		#print "Combination list====", listforcombinations
	#print "List of all the time values for this set=== \n", timeforlist #Uncomment to see the List of all Time Values
	index_for_min = np.argmin(timeforlist) # index for minimum value
	#print "Best combination Number=" , index_for_min+1
	LowestTimeBruteForce.append(timeforlist[index_for_min])
	#print "Best Time for this set--according to BruteForce Method=====================", timeforlist[index_for_min]
	#print "\nAs the lowest time among all of the time was chosen by the Brute-Force Method, Correctness of the Test case is Validated\n"
	#print "\nAccording to Bruteforce Method, The best combination is \n", listforcombinations[index_for_min] ##Uncomment to see the best combination according to Brute-force
	return "\n=======-------------Bruteforce Method Done------------============\n"
	

def GreedyAlgorithm(sets_of_person):
	global LowestTimeGreedy
	List_person = list(sets_of_person)
	List_person.sort(key=lambda x:x[1]+x[2], reverse=True)
	#print "\nBest Combination according to Greedy Algorithm ===== \n ", List_person ## Uncomment to see which combination was chosen by the Greedy Algorithm
	LowestTimeGreedy.append(CalculateTimeToFinishAll(List_person))
	#print "\nBest Time according to Greedy Algorithm ================",LowestTimeGreedy   #Uncomment to see the Lowest time for the Greedy Algorithm
	return "\n-------============ End of Greedy Algorithm ==============------ \n"


#testset=[(30,80,40),(25,40,20),(40,50,18)] # Tested with this at first
#print "Test Set [testSet]====== \n ", testset

def GenerateTestCases():
	print " \n ................. Generating test cases with 1 to 10 Campers ...................\n"
	print" \nFor 10 and 11 campers it takes around 7 and 82 seconds\nWhere 12 takes forever........Or gives a segmentation fault and Never finishes\n\n"
	for r in range(1,11):
		personset = randomTimeGenerator(r)
		print GreedyAlgorithm(personset)
		print bruteForce(personset)
		print "\nFor Test Cases of campers 1 to 10---Best Time according to Greedy Algorithm ===\n",LowestTimeGreedy
		print "For Test Cases of campers 1 to 10---Best Time according to BruteForce Method======\n", LowestTimeBruteForce 
		if LowestTimeBruteForce==LowestTimeGreedy:
			print "\nThe Designed Algorithm is giving us the correct ans\n"
		else:
			print "\n \n Something is wrong \n \n"

	N = 10
	fig2 = plt.figure()
	ind = np.arange(N) 
	width = 0.35       
	plt.bar(ind, LowestTimeBruteForce, width, label='Brute-Force')
	plt.bar(ind + width, LowestTimeGreedy, width,label='Greedy Algorithm')
	plt.gca().yaxis.grid(True) # Getting a Y axis grid
	plt.ylabel('Lowest Unit-Time required to finish the Competition')
	plt.xlabel('Number of Campers------>')
	plt.title('Validaton of Correctness of Bruteforce method and Greedy Algorithm')
	plt.xticks(ind + width / 2, ('1', '2', '3', '4', '5','6','7','8','9','10'))
	plt.legend(loc='best')
	#plt.show()
	fig2.savefig('Validation of Correctness of the Brute-Force and Greedy Algorithm.png')


def GettingTimesForGreedy():
	global GreedyTimeList
	global GreedyYaxis
	print "\n\n\n -------------- Testing the Time complexity of Greedy Algorithm -----------\n\n\n"
	for n in range(1,1001):
		personset=randomTimeGenerator(n)
		start = time.clock()  ##Start the timer
		GreedyAlgorithm(personset)
		end = time.clock()  # End the timer
		GreedyTimeList.append((end-start)*1000000) #Getting value in Micro-seconds
		GreedyYaxis.append(n)
	#print "Time List for Greedy Algorithm with increasing input size", GreedyTimeList # Uncomment to see the TimeList for Greedy with increasing input size
	fig = plt.figure()
	plt.title("Time Complexity of the Implemented Greedy Algorithm")
	plt.xlabel('Number of Campers------>>>') 
	plt.ylabel('Time Complexity in Micro-seconds------>>>') 
	plt.plot(GreedyYaxis, GreedyTimeList, label ='Greedy Algorithm') 
	plt.grid() 
	plt.legend() 
	#plt.show() 	
	fig.savefig('Time Complexity of Greedy Algorithm.png')

GenerateTestCases()

GettingTimesForGreedy()
