from nose.tools import assert_equal
class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e



def nth_to_last_node(n, head):
    curNode = head
    nNodesFromcurNode = head
    for i in range(n-1):
        if nNodesFromcurNode is None:
            raise BoundaryError("You have crossed the linked list boundary")
        nNodesFromcurNode = nNodesFromcurNode.nextnode
    while nNodesFromcurNode.nextnode:
        nNodesFromcurNode = nNodesFromcurNode.nextnode
        curNode = curNode.nextnode
    return curNode

target_node = nth_to_last_node(2, a) 

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print('ALL TEST CASES PASSED')
        
t = TestNLast()
t.test(nth_to_last_node)