from swap import swap

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        print(lyst)
        while i < n:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
            i += 1
        n -= 1

lyst = [5,4,3,2,1]
bubbleSort(lyst)
print(lyst)
