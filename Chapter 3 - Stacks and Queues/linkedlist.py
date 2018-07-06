from random import randint

class Node():
    """implementation of a simple Node object"""
    def __init__(self,data=None,next=None):
        self.next = next
        self.data = data
    def __str__(self):
        return str(self.data)


class LinkedList():
    """linked list implementation"""
    def __init__(self,lst=[]):
        self.head = None
        self.len = 0
        for n in reversed(lst):
            self.insert(n)

    def insert(self,data):
        self.head = Node(data,self.head)
        self.len += 1

    def populate(self,q=10, rng=16):
        while self.len < q:
            self.insert(randint(0,rng))

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        end = Node(data)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = end
        self.len += 1

    def deleteNode(self,n):
        cn = self.head
        if not cn:
            return False
        while cn.next:
            if cn.next == n:
                cn.next = cn.next.next
                return True
            cn = cn.next
        return False

    def deleteNode_fast(self,n):
        if not n:
            return False
        if not n.next:
            return self.deleteNode(n)
        n.data = n.next.data
        n.next = n.next.next
        return True

    def mkunique(self):
        buffer = set()
        n = self.head
        if n:
            buffer.add(n.data)
        else:
            return
        while n.next:
            if n.next.data not in buffer:
                buffer.add(n.next.data)
                n = n.next
            else:
                n.next = n.next.next
                self.len -= 1

    def print_data(self):
        n=self.head
        while n:
            print(n.data,end=', ')
            n = n.next
        print()
        if not self.head:
            print("The list is empty.")

    def __str__(self):
        l = []
        n=self.head
        while n:
            l.append(n.data)
            n = n.next
        return str(l)

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __len__(self):
        return self.len

    def deleteNodeByData(self, data):
        """ deletes the first occurance of node, containing <data> from <head> list """
        if self.head.data == data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return self
            n = n.next
        return
