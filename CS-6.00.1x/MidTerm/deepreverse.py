def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in L:
        i.reverse()
    return L



L = [[1, 2], [3, 4], [5, 6, 7]]

deep_reverse(L)
    
