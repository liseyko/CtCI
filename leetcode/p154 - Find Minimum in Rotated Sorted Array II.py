class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j and nums[i] >= nums[j]:
            m = i + (j-i) // 2
            if nums[m] < nums[i]:
                j = m
            elif nums[m] > nums[j]:
                i = m + 1
            else:
                i, j = i + 1, j - 1

        if nums:
            return nums[i]
