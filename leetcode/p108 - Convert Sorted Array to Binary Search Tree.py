# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        r_idx = len(nums) // 2
        r = TreeNode(nums[r_idx])
        r.left = self.sortedArrayToBST(nums[:r_idx])
        r.right = self.sortedArrayToBST(nums[r_idx+1:])

        return r