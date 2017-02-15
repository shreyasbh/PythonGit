def InsertionSort(lyst):
    for i in range(1,len(lyst)):
        element = lyst[i]
        j = i
        while j > 0 and lyst[j-1] > element:
            lyst[j] = lyst[j-1]
            j = j- 1
        lyst[j] = element

		
lyst = [8,7,6,5,4,3,2,1,4,5,6,7]
InsertionSort(lyst)
print(lyst)
