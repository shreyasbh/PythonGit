
from lib.linklistNode import Node
from lib.linkedListBaseClass import LinkedListBaseClass 

class LinkedListWithReverse(LinkedListBaseClass):
    def __init__(self,head):
        super().__init__(head)
    def reverseRecurse(self,cur,prev):
        if cur.next is None:
            self.head = cur
            cur.next = prev
            return
        Next = cur.next
        cur.next = prev
        self.reverseRecurse(Next, cur)
    
    def reverse(self):
        if self.head == None:
            return
        self.reverseRecurse(self.head,None)
        
        
a = Node(7)
b = Node(8)
c = Node(9)
a.next = b 
b.next = c
llr = LinkedListWithReverse(a)

llr.printList()
llr.reverse()
llr.printList()
