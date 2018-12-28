class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > s:
                s = nums[i]
            else:
                s += nums[i]
            res = max(s, res)
        return res

    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
