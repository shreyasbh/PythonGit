class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedListBaseClass:
    def __init__(self,head):
        self.head = head
        self.middleElement = None

    def printList(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next

    def intCount(self,x):
        cur = self.head
        count = 0
        while cur:
            if cur.data == x:
                count += 1
            cur = cur.next
        return count
    
    def getNth(self,index):
        count = 0
        cur = self.head
        while cur:
            if count == index:
                return cur
            count += 1
            cur = cur.next
            
    def getNthFromLast(self,n):
        ptr1 = self.head
        ptr2 = self.head
        for i in range(n-1):
            ptr2 = ptr2.next 
        while ptr2 is not None:
            nth = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return nth
    
    def deleteNodeWithOnlyNodeGiven(self,node):
        temp = node.next
        node.data = temp.data
        node.next = temp.next
        temp = None
        
    def deleteLinkedList(self):
        self.head = None
        
    def findMiddleElement(self):
        ptr1 = self.head
        ptr2 = self.head
        while ptr2 and ptr2.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        self.middleElement = ptr1
        return self.middleElement
    
    def isPalindrome(self):
        self.middleElement = self.findMiddleElement()
        revListHead = reverseList(self.head)
        cur = self.head
        while revListHead and cur:
            if revListHead.data == cur.data:
                revListHead = revListHead.next 
                cur = cur.next
            else:
                return False
        return True
        
def reverseList(head):
    cur = head
    nextNode = None
    prevNode = None
    while cur:
        nextNode = cur.next
        cur.next = prevNode
        prevNode = cur 
        cur = nextNode
    head = prevNode
    return head


    
        
        

a = Node(7)
b = Node(8)
c = Node(9)
d = Node(8)
e = Node(7)
a.next = b 
b.next = c
c.next = d
d.next = e
llr = LinkedListBaseClass(a)
#print(llr.intCount(7))
#print(llr.getNth(2).data)
#print(llr.getNthFromLast(4).data)
llr.printList()
#print(llr.deleteNodeWithOnlyNodeGiven(b))
#llr.printList()
#print(llr.findMiddleElement().data)
print(llr.isPalindrome())