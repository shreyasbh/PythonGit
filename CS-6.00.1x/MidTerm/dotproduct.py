def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    
    listC = []
    listC = [i*j for i,j in zip(listA,listB)]
    return sum(listC)

listA = [1, 2, 3]
listB = [4, 5, 6]
dotProduct(listA,listB)
                
