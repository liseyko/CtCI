# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def _pathSum(self, root, sum):
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            r = [root.val]
            while root.parent:
                r.append(root.parent.val)
                root = root.parent

            self.res.append(r[::-1])
            return

        for c in root.left, root.right:
            if c:
                c.parent = root
                self._pathSum(c, sum)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        root.parent = None
        self._pathSum(root, sum)
        return self.res