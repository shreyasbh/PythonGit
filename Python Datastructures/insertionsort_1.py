def insertionSort(lyst):
    for i in range(1, len(lyst)):
        val = lyst[i]
        j = i - 1
        while j > 0 and lyst[j] > val:
            lyst[j+1] = lyst[j]
            j -= 1
        lyst[j+1] = val

if __name__ == "__main__":
    lyst = [1,5,4,6,8,7]
    insertionSort(lyst)
    print(lyst)
