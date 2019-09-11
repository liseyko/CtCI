class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, cur = [[]], []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [lst+[n] for lst in cur]
            else:
                cur = [lst+[n] for lst in res]
            res += cur
        return res
