# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.tail = None

    def _flatten(self, root):
        for c in root.right, root.left:
            if c:
                self._flatten(c)
        print(root.val)
        root.left = None
        root.right = self.tail
        self.tail = root

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self._flatten(root)
