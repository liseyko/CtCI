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
    def _find_next(self, node):
        while node:
            for c in [node.left, node.right]:
                if c:
                    yield c
            node = node.next

    def connect(self, root, parent=None):
        if root:
            if parent:
                ptr = TreeLinkNode(-1)
                for c in self._find_next(parent):
                    ptr.next = c
                    ptr = ptr.next

            if root.left or root.right:
                if not root.left or not root.right:
                    return self.connect(root.left or root.right, root)
                self.connect(root.left, root)
                self.connect(root.right)
