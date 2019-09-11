class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = cur = 1 if nums else 0
        for i in range(len(nums)-1):
            increasing = nums[i+1] > nums[i]
            if increasing:
                cur += 1
            else:
                res, cur = max(res, cur), 1
        return max(res, cur)
