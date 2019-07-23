class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.data = [None] * self.size

    def hash(self, key):
        return ((13 * key + 50000) % 99991) % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.data[hashkey]:
            self.data[hashkey] = Node(key, value)
        else:
            node = self.data[hashkey]
            while node:
                if key == node.key:
                    node.val = value
                    return
                tail, node = node, node.next
            tail.next = Node(key, value)

    def get(self, key):
        hashkey = self.hash(key)
        node = self.data[hashkey]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        hashkey = self.hash(key)
        node = self.data[hashkey]
        if node:
            if node.key == key:
                self.data[hashkey] = node.next
            else:
                prv, cur = node, node.next
                while cur:
                    if cur.key == key:
                        prv.next = cur.next
                        return
                    prv, cur = cur, cur.next


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k = 101
        self.buckets = [[] for _ in range(self.k)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        b, i = self._getBucketAndIdx(key)
        if i is not None:
            b[i][1] = value
        else:
            b.append([key, value])

    def _getBucket(self, key):
        return self.buckets[key % self.k]

    def _getBucketAndIdx(self, key):
        b = self._getBucket(key)
        for i, kv in enumerate(b):
            if kv[0] == key:
                return b, i
        return b, None

    def get(self, key: int) -> int:
        b, i = self._getBucketAndIdx(key)
        if i is not None:
            return b[i][1]
        return -1

    def remove(self, key: int) -> None:
        b, i = self._getBucketAndIdx(key)
        if i is not None:
            del b[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
