from swap import swap

def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j= i + 1
        print(lyst)
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1

lyst = [5,4,3,2,1]
selectionSort(lyst)
print(lyst)
