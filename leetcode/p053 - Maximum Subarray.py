class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ms = float('-inf')
        cs = ms
        for n in nums:
            if n > cs + n:
                cs = n
            else:
                cs +=  n
            ms = max(ms, cs)
        return ms
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)