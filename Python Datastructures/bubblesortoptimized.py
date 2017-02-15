def BubbleSort(lyst):
	i = 0
	swap = 0
	while i < len(lyst):
		for j in range(len(lyst)-1-i):
			if lyst[j] > lyst[j+1]:
				lyst[j], lyst[j+1] = lyst[j+1], lyst[j]
				swap += 1 
		i += 1
		if swap == 0:
			break

		
lyst = [1,9,8,7,6,5,4,3,2]
BubbleSort(lyst)
print(lyst)
