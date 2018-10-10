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

class Solution: # more efficient
    def _sortedArrayToBST(self, l, r):
        if r - l < 0:
            return None
        root_idx = (r + l) // 2
        root = TreeNode(self.nums[root_idx])
        if r - l > 0:
            root.left = self._sortedArrayToBST(l, root_idx-1)
            root.right = self._sortedArrayToBST(root_idx+1, r)
        return root
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        self.nums = nums
        return self._sortedArrayToBST(0, len(nums)-1)