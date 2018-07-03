""" partition linked list [nodes < x <= nodes] """

from linkedlist import LinkedList
from random import randint


def ll2N(ll):
    n = 0
    p = 0
    for d in ll:
        n += d.data*10**p
        p += 1
    return n

def n2LL(n):
    ll = LinkedList()
    while n > 0:
        ll.append(n%10)
        n = n // 10
    return ll

def sumLL(ll1,ll2):
    return n2LL(ll2N(ll1) + ll2N(ll2))


def ll2N_fw(ll):
    """reverse Linked List"""
    ptr1=ll.head
    if ptr1:
        ptr2=ptr1.next
        ptr1.next = None
    while ptr2:
        tmp = ptr2.next
        ptr2.next = ptr1
        ptr1 = ptr2
        ptr2 = tmp
    ll.head = ptr1
    return ll2N(ll)

def n2LL_fw(n):
    ll = LinkedList()
    while n > 0:
        ll.insert(n%10)
        n = n // 10
    return ll

def sumLL_fw(ll1,ll2):
    return n2LL_fw(ll2N_fw(ll1) + ll2N_fw(ll2))

def sumLL_opt(ll1,ll2):
    s = 0
    s1 = ll1.head
    s2 = ll2.head
    rl = LinkedList()
    while s1 or s2:
        if s1:
            s += s1.data
            s1 = s1.next
        if s2:
            s += s2.data
            s2 = s2.next
        rl.append(s%10)
        s = s // 10
    if s > 0:
        rl.append(s)
    return(rl)


def sumLL_fw_opt(ll1,ll2):
    ldiff = ll1.len - ll2.len
    if ldiff < 0:
        for _ in range(abs(ldiff)):
            ll1.insert(0)
    elif ldiff > 0:
        for _ in range(ldiff):
            ll2.insert(0)
    print(ll1,'\n',ll2,sep='')
    r = LinkedList()
    s=0
    d1=ll1.head
    d2=ll2.head
    r.append(0)
    pptr = r.head
    while d1:
        s = d1.data + d2.data
        r.append(s%10)
        pptr.data+=s//10
        pptr = pptr.next
        d1 = d1.next
        d2 = d2.next
    if r.head.data == 0:
        r.head = r.head.next
    return r




for i in range(5):
    n = randint(90,320)
    ll = n2LL(n)
    n1 = ll2N(ll)
    print(n,ll,n1)

i1 = LinkedList([7,1,6])
i2 = LinkedList([5,9,2])
print("test:\n",i1,'\n',i2,sep='')
print(sumLL(i1,i2))
print(sumLL_opt(i1,i2))

i1 = LinkedList([8,8,8,1])
i2 = LinkedList([5,9,2])
print(sumLL(i1,i2))
print(sumLL_opt(i1,i2))


print("forward order:")
for i in range(5):
    n = randint(90,320)
    ll = n2LL_fw(n)
    print(n,ll,end=',')
    n1 = ll2N_fw(ll)
    print(n1)

i1 = LinkedList([6,1,7])
i2 = LinkedList([2,9,5])
print("test:\n",i1,'\n',i2,sep='')
#print(sumLL_fw(i1,i2))
print(sumLL_fw_opt(i1,i2))
