"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        lvl = collections.deque([root])
        while any(lvl):
            for i in range(1, len(lvl)):
                lvl[i-1].next = lvl[i]
            lvl = [c for n in lvl for c in (n.left, n.right) if c]
        return root

    def connect(self, root: 'Node') -> 'Node':
        head = node = root if root else Node(0, None, None, None)
        while head.left:
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next

            head = node = head.left

        return root
