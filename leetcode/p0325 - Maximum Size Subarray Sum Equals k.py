"""
The idea is that if there is a number in a map where sum less k equals
to a number already in a table, there must be a contiguous section
from that point (mp[acc - k]) to current point (i)
where the sum of all items is k. The distance between these two points
is the length of the subarray, and is a candidate for our answer.
"""


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans, acc = 0, 0
        mp = {0: -1}
        for i, n in enumerate(nums):
            acc += n
            if acc not in mp:
                mp[acc] = i
            if acc-k in mp:
                ans = max(ans, i - mp[acc-k])

        return ans
