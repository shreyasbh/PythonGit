def betterLinearSearch(lyst,item):
    flag = 0
    for i in range(len(lyst)):
        if lyst[i] == item:
            flag = 1
            return flag
    return flag

if __name__ == "__main__":
    lyst = [1,2,3,4,5,6]
    item = 1

    ret = betterLinearSearch(lyst,item)
    if ret == 1:
        print("Item found")
    else:
        print("Item not found")
