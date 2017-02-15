from swap import swap 

def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i-1
        while j >=0 :
            if itemToInsert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = itemToInsert
        i += 1

lyst = [4,5,6,1,2,3]
insertionSort(lyst)
print(lyst)
