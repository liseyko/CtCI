class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def print(self):
        n = self
        while n:
            print(n.val, '->', end='')
            n = n.next
        print()


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.tail = None
        self.len = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        n = self.head
        while n and index:
            n, index = n.next, index-1
        return getattr(n, 'val', -1)

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the
        linked list.
        :type val: int
        :rtype: void
        """
        if self.head:
            n = Node(val, self.head)
            self.head = n
        else:
            self.head = self.tail = Node(val)
        self.len += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.tail:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(val)
        self.len += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the
        length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if not index:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else:
            n = self.head
            while n and index-1:
                n, index = n.next, index-1
            if n:
                n.next = Node(val, n.next)
                self.len += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if not index and self.head:
            self.head = self.head.next
        n = self.head
        while n and index-1:
            n, index = n.next, index-1
        if n and n.next:
            n.next = n.next.next
            self.len -= 1
            if not n.next:
                self.tail = n


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
