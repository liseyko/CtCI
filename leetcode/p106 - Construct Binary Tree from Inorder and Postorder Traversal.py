import bisect
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = TreeNode(postorder.pop()) if postorder else None
        if not postorder:
            return root

        splitIdx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:splitIdx], postorder[:splitIdx])
        root.right = self.buildTree(inorder[splitIdx+1:], postorder[splitIdx:])
        return root
