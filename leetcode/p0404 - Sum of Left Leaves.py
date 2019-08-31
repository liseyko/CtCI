# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def _isLeaf(node):
            return node and not node.left and not node.right

        def _sumLeftLeafs(root=root):
            if not root:
                return
            if _isLeaf(root.left):
                self.res += root.left.val
            else:
                _sumLeftLeafs(root.left)
            _sumLeftLeafs(root.right)

        self.res = 0
        _sumLeftLeafs()
        return self.res
