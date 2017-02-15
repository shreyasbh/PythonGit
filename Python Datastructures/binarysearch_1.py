def binarySearch(lyst,item):
    flag = 0
    start = 0
    end = len(lyst)
    while start < end:
        mid = (start+end)//2
        print(mid)
        if item > lyst[mid]:
            start = mid+1
            print(lyst[start:])
            binarySearch(lyst[start:],item)
        elif item < lyst[mid]:
            end  = mid
            binarySearch(lyst[:end],item)
            print(lyst[:end])
        elif lyst[mid] == item:
            flag = 1
            return flag

if __name__ == "__main__":
    lyst = [1,2,3,4,5,6]
    item = 4
    ret = binarySearch(lyst,item)
    if ret == 1:
        print("Item Found")
    else:
        print("Item not found")
