import lib.linkedList

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data

class LinkedList(object):
    def __init__(self,head):
        self.head = head
    def printList(self):
        curNode = self.head
        if curNode == None:
            return
        while curNode.next != None:
            print(curNode.getData())
            curNode = curNode.next
        print(curNode.getData())
    def addNode(self,node,position):
        if self.head == None:
            self.head = node
            return
        curNode = self.head
        curPosition = 0
        if position == 0:
            node.next = curNode
            self.head = node
            return
        while curPosition != position:
            if curNode == None:
                print("Element Out of bounds")
                return
            prevNode = curNode
            curNode = curNode.next
            curPosition += 1
        prevNode.next = node
        node.next = curNode
    def delNode(self,position):
        if position == 0:
            self.head = self.head.next
            return
        curPosition = 0
        curNode = self.head
        while curPosition != position:
            prevNode = curNode
            curNode = curNode.next
            curPosition += 1
            if curNode == None:
                print("Element Out of bounds")
                return
        prevNode.next = prevNode.next.next        
        


a = Node(5)
b = Node(6)
c = Node(7)

a.next = b
b.next = c

ll = LinkedList(a)
ll.printList()

 

ll.addNode(Node(8),0)
print("After adding 8")
ll.printList()
print("After adding 9")
ll.addNode(Node(9),4)
ll.printList()
ll.delNode(0)
print("Deleting First Element")
ll.printList()
ll.delNode(0)
print("Deleting Second Element")
ll.printList()


    
        
