#from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.inorderTraversal(root.left)
        self.res.append(root.val)            
        self.inorderTraversal(root.right)
        return self.res


    def inorderTraversal(self, curr):
        res, stk = [], []

        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            res.append(curr.val)
            curr = curr.right

        return res

    #def inorderTraversal(self, curr):
        # TODO: Morris Traversal