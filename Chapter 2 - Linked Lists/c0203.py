""" delete a node in the middle of a singly linked list, given only access to this node """

from linkedlist import LinkedList


def deleteNode(n):
    if not n or not n.next:
        return False
    n.data = n.next.data
    n.next = n.next.next
    return True


l1=LinkedList()
l1.populate(7)
print(l1)

m=l1.head
for _ in range(l1.size//2):
    m=m.next
print(m.data)
deleteNode(m)
print(l1)