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
        return ((13 * key + 50000) % 99991 ) % self.size

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
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        node = self.data[hashkey]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
    
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
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
