class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def reverse(head):
    curNode = head
    nextNode = prevNode = None
    
    while curNode != None:
        nextNode = curNode.nextnode
        curNode.nextnode = prevNode
        prevNode = curNode
        curNode = nextNode
    return prevNode

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d
        
reverse(a)

print(b.nextnode.value)

