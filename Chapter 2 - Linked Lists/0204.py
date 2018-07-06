""" partition linked list [nodes < x <= nodes] """

from linkedlist import LinkedList
from random import randint

def partitionList0(l,m):
    lp = LinkedList()
    for n in l:
        if n.data < m:
            lp.insert(n.data)
        else:
            lp.append(n.data)
    return lp

def partitionList(l,m):
    n = l.head
    while n:
        if n.data < m:
            l.insert(n.data)
            nd = n
            n = n.next
            l.deleteNode(nd)
        else:
            n = n.next
    return

def partitionList2(l,m):
    lb = LinkedList()
    la = LinkedList()
    for n in l:
        if n.data < m:
            lb.insert(n.data)
        else:
            la.insert(n.data)
    if not lb.head:
        return la
    n = lb.head
    while n.next:
        n = n.next
    n.next = la.head
    return lb


l1 = LinkedList()
l1.populate(9)
print(l1)
x = randint(1,16)
print("partition point:",x)
l2 = partitionList0(l1,x)
print(l2)
l3 = partitionList2(l1,x)
print(l3)
partitionList(l1,x)
print(l1)
