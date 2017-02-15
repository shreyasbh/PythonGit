def bubbleSort(lyst):
    for i in range(len(lyst)):
        for j in range(len(lyst)-i-1):
            if lyst[j] > lyst[j+1]:
                lyst[j], lyst[j+1] = lyst[j+1], lyst[j]
    return lyst

if __name__ == "__main__":
    lyst = [2,1,4,3,9,5,6]
    retList = bubbleSort(lyst)
    print(lyst)
