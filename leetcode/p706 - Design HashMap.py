class Node:
    def __init__(self, key=None, val=None):
        self.next = None
        self.key, self.val = key, val


class MyHashMap:
    def __init__(self):
        self.size = 4096
        self.cache = [None for _ in range(self.size)]

    def _getLList(self, key):
        # idx = key % self.size
        idx = 0x811c9dc5
        prime = 0x01000193
        idx = (idx ^ key * prime) % self.size
        if not self.cache[idx]:
            self.cache[idx] = Node()
        return self.cache[idx]

    def _getParentOfKeyNode(self, key):
        pn = self._getLList(key)
        while pn.next:
            if pn.next.key == key:
                break
            pn = pn.next
        return pn

    def put(self, key: int, value: int) -> None:
        pn = self._getParentOfKeyNode(key)
        if pn.next:
            pn.next.val = value
        else:
            pn.next = Node(key, value)

    def get(self, key: int) -> int:
        pn = self._getParentOfKeyNode(key)
        return pn.next.val if pn.next else -1

    def remove(self, key: int) -> None:
        pn = self._getParentOfKeyNode(key)
        if pn.next:
            pn.next = pn.next.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
