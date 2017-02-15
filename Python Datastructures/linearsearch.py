def linearSearch(lyst,item):
    flag = 0
    for i in range(len(lyst)):
        if lyst[i] == item:
            flag = 1
    if flag == 1:
        print("Item found")
    else:
        print("Item not found")

lyst = [1,2,3,4,5]
item = 6
linearSearch(lyst,item)
