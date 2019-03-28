"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, node):
        result = node
        head = tail = Node(0)
        while node:
            for c in (node.left, node.right):
                tail.next = c
                if c:
                    tail = tail.next
            if node.next:
                node = node.next
            else:
                node, tail = head.next, head
        return result

    def connect(self, root: 'Node') -> 'Node':
        parent = root
        head = tail = Node(0, None, None, None)

        while parent:
            for child in [c for c in (parent.left, parent.right) if c]:
                tail.next = child
                tail = tail.next

            parent = parent.next
            if not parent:
                tail, parent = head, head.next
                head.next = None

        return root
