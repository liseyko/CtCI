class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = csum = sum(nums[:k])
        for i, n in enumerate(nums[k:]):
            csum = csum + n - nums[i]
            res = max(res, csum)
        return res / k
