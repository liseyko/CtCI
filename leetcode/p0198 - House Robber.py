class Solution:
    def rob(self, nums: List[int]) -> int:
        nums += [0]*2
        for i in range(2, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-2:])

    def rob(self, nums: List[int]) -> int:
        prv = cur = 0
        for n in nums:
            prv, cur = cur, max(cur, prv+n)
        return cur
