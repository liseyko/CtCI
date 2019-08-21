# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.heights = {}

    def getHeight(self, root):
        if root in self.heights:
            return self.heights[root]
        if not root:
            self.heights[root] = 0
        else:
            self.heights[root] = \
              1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return self.heights[root]

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if self.isBalanced(root.left) \
           and self.isBalanced(root.right) \
           and abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2:
            return True
        return False


class Solution:
    def dfsHeight(self, root):
        if not root or not self.balanced:
            return 0
        lHeight = self.dfsHeight(root.left)
        rHeight = self.dfsHeight(root.right)
        if abs(lHeight - rHeight) > 1:
            self.balanced = False
        return 1 + max(lHeight, rHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        self.dfsHeight(root)
        return self.balanced
