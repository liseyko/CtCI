class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maX, suM = max(nums), sum(nums)

        for i in range(maX+1):
            suM -= i
        if not suM and len(nums)-1 == maX:
            return maX + 1
        return abs(suM)

    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
