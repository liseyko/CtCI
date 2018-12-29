class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax = currMax = 0
        for n in nums:
            prevMax, currMax = currMax, max(prevMax + n, currMax)
        return currMax
