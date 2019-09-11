class NumStr(str):
    def __lt__(self, other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            nums = sorted([str(x) for x in nums], key = NumStr)
            return ''.join(nums).lstrip('0') or '0'
