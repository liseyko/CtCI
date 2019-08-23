# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxN, maxIdx = float('-inf'), -1
        for i, n in enumerate(nums):
            if n > maxN:
                maxN, maxIdx = n, i

        root = TreeNode(maxN)
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root
