# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        lvl, res = [root], []
        while any(lvl):
            res.append([node.val for node in lvl])
            lvl = [chld for node in lvl
                   for chld in (node.left, node.right) if chld]
        return res
