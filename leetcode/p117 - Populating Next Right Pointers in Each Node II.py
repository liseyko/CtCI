# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, node):
        head = tail = TreeLinkNode(0)
        while node:
            for c in (node.left, node.right):
                tail.next = c
                if c:
                    tail = tail.next
            if node.next:
                node = node.next
            else:
                node, tail = head.next, head

    def connect(self, root):
            while root:
                cur = tmp = TreeLinkNode(0)
                while root:
                    if root.left:
                        cur.next = root.left
                        cur = root.left
                    if root.right:
                        cur.next = root.right
                        cur = root.right
                    root = root.next
                root = tmp.next
