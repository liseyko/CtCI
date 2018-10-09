# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = False
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if self.res or not root:
            return self.res

        sum -= root.val
        
        if sum == 0 and not root.left and not root.right:
            self.res = True
            return self.res
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)