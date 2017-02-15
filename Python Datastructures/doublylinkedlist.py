class Node(object):
    def __init__(self, data = None, nnext = None, prev = None):
        self.data = data
        self.next = nnext
        self.prev = prev
    def setData(self,data):
        self.data = data
    def getData(self,data):
        return self.data
    def setNext(self,nnext):
        self.next = nnext
    def getNext(self):
        return self.next
    def setPrev(self,prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def hasNext(self):
        return self.next != None
    def hasPrev(self):
        return self.prev != None


class DoublyLinkedList(object):
    def __init__(self,head):
        self.head = head
    def insertAtBegining(self,data):
        new = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = new
        else:
            new.setNext(self.head)
            self.head.setPrev(new)
            self.head = new
    def insertAtEnd(self,data):
        new = Node(data, None, None)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while current.hasNext():
                current = current.getNext()
            current.setNext(Node(data,None, current))
            self.tail = current.getNext()
    def getNode(self,index):
        current = self.head
        if currentNode == None:
            return None
        count = 0
        while count <= index:
            currentNode = currentNode.getNext()
            if currentNode == None:
                break
            i += 1
        return currentNode
    def insertAtPosition(self,index,data):
        new = Node(data)
        if self.head == None or index == 0:
            self.insertAtBegining(data)
        elif index > 0:
            temp = self.getNode(index):
            if temp == None or temp.getNext() == None:
                self.insertAtEnd(data)
            else:
                new.setNext(temp.getNext())
                new.setPrev(tmp)
                temp.getNext().setPrev(new)
                temp.setNext(new)
    def deleteAtPosition(self,position):
        temp = self.getNode(position)
        if temp:
            temp.getPrev().setNext(temp.getNext())
            if temp.getNext():
                temp.getNext().setPrev(temp.getPrev())
            temp.setPrev(None)
            temp.setNext(None)
            temp.setData(None)
    def deleteData(self,data):
        temp = self.head
        while temp != None:
            if temp.getData() == data:
                if temp.getPrev() != None:
                    self.head = temp.getNext()
                    temp.getNext().setPrev(None)
                else:
                    temp.getPrev().setNext(temp.getNext())
                    temp.getNext().setPrev(temp.getPrev())
            temp = temp.getNext()
        
        


