class Solution:
    def _rob(self, nums: List[int]) -> int:
        prv = cur = 0
        for n in nums:
            prv, cur = cur, max(cur, prv+n)
        return cur

    def rob(self, nums: List[int]) -> int:
        return max(self._rob(nums[:-1]), self._rob(nums[1:]),
                   nums[0] if nums else 0)
