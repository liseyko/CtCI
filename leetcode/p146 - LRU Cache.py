class Node:
    def __init__(self, key=None, val=None):
        self.prev, self.next = None, None
        self.key, self.val = key, val

    def pop(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self


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
            self.nodes[key] = Node(key, value)
            self._refresh(key, newNode=True)

    def _refresh(self, key: int, newNode=False) -> None:
        if newNode:
            self._popright()
        else:
            self.nodes[key].pop()
        self._appendleft(self.nodes[key])

    def _appendleft(self, n: Node) -> None:
        n.next, n.prev = self.head.next, self.head
        self.head.next = n.next.prev = n

    def _popright(self) -> None:
        if len(self.nodes) > self.cap:
            del self.nodes[self.tail.prev.pop().key]


class Node:
    def __init__(self, val):
        self.prev, self.next = None, None
        self.val = val

    def pop(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv, self.kn = {}, {}  # key: val, key: node
        self.head, self.tail = Node('^'), Node('$')
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self.refresh(key)
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        self.kv[key] = value
        self.refresh(key)

    def refresh(self, key: int) -> None:
        if key in self.kn:
            n = self.kn[key].pop()
        else:
            n = self.kn[key] = Node(key)
        self.appendleft(n)
        self.trim()

    def appendleft(self, n):
        n.next, n.prev = self.head.next, self.head
        self.head.next = n.next.prev = n

    def trim(self):
        if len(self.kn) > self.cap:
            key = self.tail.prev.pop().val
            del self.kv[key]
            del self.kn[key]
