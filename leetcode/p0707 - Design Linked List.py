class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class MyLinkedList:

    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if not self._isValidIdx(index):
            return -1
        ptr = self.head.next
        for _ in range(index):
            ptr = ptr.next
        return ptr.val

    def addAtHead(self, val: int) -> None:
        self._addAfter(self.head, val)

    def addAtTail(self, val: int) -> None:
        self._addAfter(self.tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        if not self._isValidIdx(index):
            return

        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        self._addAfter(ptr, val)

    def deleteAtIndex(self, index: int) -> None:
        if not self._isValidIdx(index):
            return

        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        self._delAfter(ptr)

    def _isValidIdx(self, index):
        return -1 < index < self.size

    def _addAfter(self, node, val):
        newNode = Node(val, node.next)
        node.next = newNode
        if node == self.tail:
            self.tail = node.next
        self.size += 1

    def _delAfter(self, node):
        if node.next == self.tail:
            self.tail = node
        node.next = node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
