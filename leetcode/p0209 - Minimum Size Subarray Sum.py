class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        lp = 0
        csum = 0
        res = float('inf')
        for rp in range(len(nums)):
            csum +=nums[rp]
            if csum < s:
                continue
            while csum - nums[lp] >= s:
                csum -= nums[lp]
                lp += 1
            res = min(res, rp+1-lp)
        return res if res != float('inf') else 0
