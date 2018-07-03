from random import randint

class Node():

    def __init__(self,data=None,next=None):
        self.next = next
        self.data = data


class LinkedList():

    def __init__(self,lst=[]):
        self.head = None
        self.size = 0
        for n in reversed(lst):
            self.insert(n)

    def insert(self,data):
        self.head = Node(data,self.head)
        self.size += 1

    def populate(self,q=10, rng=16):
        while self.size < q:
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
        self.size += 1

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

    def deleteNode(self, data):
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

