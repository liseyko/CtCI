# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.balanced = True

    def getHeight(self, root):
        if not self.balanced:
            return -1
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if abs(l - r) > 1:
           self.balanced = False

        return 1 + max(l, r)


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.getHeight(root)
        return self.balanced


class Solution:
    def __init__(self):
        self.depths = {}
    def getDepth(self, root):
        if root in self.depths:
            return self.depths[root]
        if not root:
            self.depths[root] = 0
        else:
            self.depths[root] = 1 + max(self.getDepth(root.left), self.getDepth(root.right))
        return self.depths[root]

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if self.isBalanced(root.left) \
            and self.isBalanced(root.right) \
            and abs(self.getDepth(root.left) - self.getDepth(root.right)) < 2:
                return True
        return False
