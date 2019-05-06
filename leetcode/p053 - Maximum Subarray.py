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

    def maxSubArray(self, nums: List[int]) -> int:
        result = currentSum = nums[0] if nums else None
        for n in nums[1:]:
            currentSum = max(currentSum + n, n)
            result = max(result, currentSum)
        return result
