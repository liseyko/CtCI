# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def _isUnival(root):
            if not root:
                return True
            leftIsUnival = _isUnival(root.left)
            rightIsUnival = _isUnival(root.right)
            if root.left and (not leftIsUnival or root.left.val != root.val)\
               or root.right and (not rightIsUnival or root.right.val != root.val):
                return False
            self.result += 1
            return True

        self.result = 0
        _isUnival(root)
        return self.result
