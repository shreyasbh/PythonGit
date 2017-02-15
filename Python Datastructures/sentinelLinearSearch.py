def sentinelLinearSearch(lyst,item):
    temp = lyst[-1]
    lyst[-1] = item
    i = 0
    while (lyst[i] != item):
        i += 1
    if i < len(lyst) - 1:
        print("Item Found")
    elif temp == item:
        print("Item found")
    else:
        print("Item not found")

if __name__ == "__main__":
    lyst = [1,2,3,4,5,6]
    item = 1
    sentinelLinearSearch(lyst,item)
