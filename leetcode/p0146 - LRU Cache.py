class Node:
    def __init__(self, key=None, val=None):
        self.prev, self.next = None, None
        self.key, self.val = key, val


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self._refresh(key)
        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self._refresh(key)
        else:
            self._popWhenFull()
            self.nodes[key] = Node(key, value)
            self._refresh(key, newNode=True)

    def _refresh(self, key: int, newNode=False) -> None:
        if not newNode:
            self._unlink(self.nodes[key])
        self._appendleft(self.nodes[key])

    def _appendleft(self, n: Node) -> None:
        n.next, n.prev = self.head.next, self.head
        self.head.next = n.next.prev = n

    def _popWhenFull(self) -> None:
        if len(self.nodes) == self.cap:
            oldestNode = self.tail.prev
            del self.nodes[oldestNode.key]
            self._unlink(oldestNode)

    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
