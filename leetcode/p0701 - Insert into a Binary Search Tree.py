# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def find(r=root, p=None, v=val):
            if not r:
                return p
            if v > r.val:
                return find(r.right, r)
            elif v < r.val:
                return find(r.left, r)

        if not root:
            return TreeNode(val)
        n = TreeNode(val)
        p = find()

        if n.val > p.val:
            n.right, p.right = p.right, n
        else:
            n.left, p.left = p.left, n

        return root
