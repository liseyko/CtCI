class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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