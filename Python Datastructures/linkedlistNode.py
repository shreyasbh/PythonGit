class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next

    def addNodeBegining(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def addNodeAfter(self, prevNode, newData):
        if prevNode == None:
            print("The node is not in List")

        newNode = Node(newData)

        newNode.next = prevNode.next
        prevNode.next = newNode

    def addNodeAtEnd(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return

        end = self.head
        while(end.next):
            end = end.next

        end.next = newNode

    def deleteNode(self,key):

        t = self.head

        if t != None:
            if t.data == key:
                self.head = t.next
                t = None
                return

        while t != None:
            if t.data == key:
                break
            prev = t
            t = t.next

        if t == None:
            return

        prev.next = t.next

        t = None


llist = LinkedList()
llist.addNodeBegining(7)
llist.addNodeBegining(1)
llist.addNodeBegining(3)
llist.addNodeBegining(2)
llist.printList()
llist.deleteNode(1) 
llist.printList()



    


        
