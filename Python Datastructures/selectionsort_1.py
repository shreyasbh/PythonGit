def selectionSort(lyst):
    for i in range(len(lyst)-1):
        smallest = lyst[i]
        smallLoc = i
        for j in range(i+1, len(lyst)):
            if lyst[j] < smallest:
                smallest = lyst[j]
                smallLoc = j
        lyst[i], lyst[smallLoc] = lyst[smallLoc], lyst[i]

if __name__ == "__main__":
    lyst = [1,3,5,2,4,6,10,8,5]
    selectionSort(lyst)
    print(lyst)
            
            
