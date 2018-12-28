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
        if not nums:
            return None
        ci = len(nums) // 2
        root = TreeNode(nums[ci])
        root.left = self.sortedArrayToBST(nums[:ci])
        root.right = self.sortedArrayToBST(nums[ci+1:])
        return root

    def sortedArrayToBST(self, nums):
        def _sortedArrayToBST(li=0, ri=len(nums)-1):
            if ri - li < 0:
                return None
            ci = li + (ri - li) // 2
            root = TreeNode(nums[ci])
            if ri - li > 0:
                root.left = _sortedArrayToBST(li, ci-1)
                root.right = _sortedArrayToBST(ci+1, ri)
            return root
        return _sortedArrayToBST()
