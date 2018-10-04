import sys
from collections import deque

"""
class QNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, key):
        if self.tail:
            self.tail.next = QNode(key)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = QNode(key)
            self.tail = self.head
    def del(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
"""

def pf(mem_limit, pages):
    pq = deque()
    pfc = 0
    pmem = set()
    #pmalloc = dict()
    
    for p in pages:
        if p not in pmem:
            pfc += 1
            pmem.add(p)
            pq.append(p)
            if len(pmem) > mem_limit:
                pmem.remove(pq.popleft())
        else:
            pq.remove(p)
            pq.append(p)
    return pfc
        

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        sys.stdin.readline()
        pages = list(map(int,sys.stdin.readline().split()))
        mem_size = int(sys.stdin.readline())
        print(pf(mem_size, pages))