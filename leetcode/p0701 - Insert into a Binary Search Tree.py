# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        n, newNode = root, TreeNode(val)
        while n:
            if val > n.val:
                p, n, loc = n, n.right, 'right'
            else:
                p, n, loc = n, n.left, 'left'
        if root:
            setattr(p, loc, newNode)
        else:
            root = newNode
        return root
