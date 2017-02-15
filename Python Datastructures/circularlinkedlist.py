class Node(object):
    def __init__(self, data = None, nnext = None):
        self.data = data
        self.next = nnext
    def setData(self,data):
        self.data = data
    def getData(self,data):
        return self.data
    def setNext(self,nnext):
        self.next = nnext
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None

class CircularlyLinkedList(object):
    def __init__(self,head):
        self.head = head
    def circular
