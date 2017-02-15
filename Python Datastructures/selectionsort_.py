def SelectionSort(lyst):
	for i in range(len(lyst)):
		min = lyst[i]
		minIndex = i
		for j in range(i+1,len(lyst)):
			if lyst[j] < min:
				min = lyst[j]
				minIndex = j
		if lyst[i] != min:
			lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]

		
lyst = [8,7,6,5,4,3,2,1]
SelectionSort(lyst)
print(lyst)
