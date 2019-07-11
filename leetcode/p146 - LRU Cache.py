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


class Node:
    def __init__(self, val):
        self.next, self.prev = None, None
        self.val = val


class LRUCache:
    """ First Attempt """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.tail = None
        self.data = {}
        self.ll = {}

    def upd(self, key):
        if key not in self.ll:
            self.ll[key] = Node(key)
        if self.ll[key] == self.head:
            return
        if not self.head:
            self.head = self.tail = self.ll[key]
            return
        if self.ll[key].prev:
            self.ll[key].prev.next = self.ll[key].next
            if self.ll[key].next:
                self.ll[key].next.prev = self.ll[key].prev
        if self.ll[key] == self.tail:
            self.tail = self.ll[key].prev
        if self.head:
            self.head.prev = self.ll[key]
        self.ll[key].next = self.head
        self.head = self.ll[key]
        if len(self.ll) > self.cap:
            key = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            del self.data[key]
            del self.ll[key]

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.upd(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.upd(key)
