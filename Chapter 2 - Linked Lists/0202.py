""" find the kth to last element of a singly linked list """
from random import randint

from linkedlist import LinkedList

N_OF_ELEMENTS = 8
k = randint(1,N_OF_ELEMENTS)
l1 = LinkedList()
l1.populate(N_OF_ELEMENTS)
print(l1)

#Sol 1
t = 0
n = l1.head
while n:
    n = n.next
    t+=1

n = l1.head
for _ in range(t-k):
    n = n.next
print(k,"(th) element to the last is:",n.data)

#Sol 2 (2 pointers. optimal)
t = 0
p1 = l1.head
p2 = p1
while p1 and t < k:
    p1 = p1.next
    t += 1
while p1:
    p1 = p1.next
    p2 = p2.next
print(k,"(th) element to the last is:",p2.data)


#Sol 3 (recursive)
n = l1.head
def getk(k,n):
    if n.next:
        j,nk = getk(k,n.next)
        if k > j:
            return (j+1,n)
        else:
            return (j,nk)
    else:
        return (1,n)

print(k,"(th) element to the last is:",getk(k,n)[1].data)
