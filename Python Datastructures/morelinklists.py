class Node(object):
    
    def __init__(self,value):

        self.value = value
        self.nextnode = None
        
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.nextnode.value)

class DoublyLinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.prevnode = None
        self.nextnode = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.nextnode = b
b.nextnode = c
b.prevnode = a
c.prevnode = b

print(a.nextnode.prevnode.value)
