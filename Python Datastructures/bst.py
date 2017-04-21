class Node(object):
    
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
        
class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)
    
    def insertNode(self,data,node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)
                
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
    
    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data
        
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data
        
    def traverse(self):
        if self.root:
            return self.inroderTraverse(self.root)
    
    def inroderTraverse(self,node):
        if node.leftChild:
            self.inroderTraverse(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.inroderTraverse(node.rightChild)
            
    def removeNode(self,data,node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:  
                print("Deleting lead node..")
                del node
                return None
            
            if not node.leftChild:
                print("Removing node with single right child")
                temp = node.rightChild
                del node
                return temp
            elif not node.rightChild:
                print("Removing node with single left child")
                temp = node.leftChild
                del node
                return temp
                
            print("Removing node with two child nodes")
            temp = self.getPredecessor()
            node.data = temp.data 
            node.leftChild = self.removeNode(temp.data, node.leftChild)
            
        return node 
        
    def getPredecessor(self):
        if node.rightChild:
            self.getPredecssor(node.rightChild)
        return node
        
    def remove(self,data):
        if self.root:
            self.removeNode(data, self.root)
        
bst = BinarySearchTree()
bst.insert(10)
bst.insert(15)
bst.insert(5)
bst.insert(6)
bst.insert(28)
bst.traverse()
print(bst.getMinValue())
print(bst.getMaxValue())
        
        
        
            