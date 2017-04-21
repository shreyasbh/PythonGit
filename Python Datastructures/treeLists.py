def binaryTree(r):
    return [r,[],[]]
    
def insertLeft(r,newBranch):
    t = r.pop(1)
    if len(t) > 1:
        r.insert(1, [newBranch, t, []])
    else:
        r.insert(1, [newBranch,[],[]])
        
    return r
    
def insertRight(r, newBranch):
    t = r.pop(2)
    
    if len(t) > 1:
        r.insert(2, [newBranch,[],t])
    else:
        r.insert(2, [newBranch,[],[]])
        
def getRootValue(r):
    return r[0]
    
def setRootValue(r,newValue):
    r[0] = newValue
    
def leftChild(r):
    return r[1]
    
def rightChild(r):
    return r[2]