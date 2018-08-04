from collections import deque

from avltree import AVLTree

class LLNode():
    def __init__(self,key,next=None):
        self.key = key
        self.next = next

class LinkedList():
    def __init__(self, data=None):
        self.head = None
        self.tail = self.head
        if data:
            for k in data:
                self.append(k)

    def append(self, key):
        n = LLNode(key)
        if not self.head:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n



def bfsTreeToLOfLL(t):
    if not t.root:
        return None
    result = [LinkedList()]
    lvl = 0
    lvl_size = 1
    q = deque([t.root])
    while len(q) > 0:
        n = q.popleft()
        lvl_size-=1
        result[lvl].append(n.key)
        for c in n.l, n.r:
            if c:
                q.append(c)
        if lvl_size == 0:
            lvl+=1
            lvl_size = len(q)
            if lvl_size > 0:
                #print(f'level: {lvl}')
                result.append(LinkedList())
    return result




if __name__ == '__main__':

    t = AVLTree([1,2,3,4,5,6,7])
    d = 0
    for ll in bfsTreeToLOfLL(t):
        print(f'\ndepth {d}:')
        llptr = ll.head
        while llptr:
            print(llptr.key,end=',')
            llptr = llptr.next
        d += 1