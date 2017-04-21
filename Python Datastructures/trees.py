class BinaryTree(Object):
    
    def __init__(self,rootObj):
        
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.left == None
            slef.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        
    def insertRight(self,newNode):
        if self.right = None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
        
    def getLeftChild(self):
        return self.leftChild
        
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self,obj):
        return self.key
        
def preorder(tree):
    if tree:
        print(getRootval(tree))
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(getRootval(tree))
        
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(getRootval(tree))
        inorder(tree.getRightChild())