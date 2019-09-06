class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set(i+1 for i in range(len(nums)))
        for n in nums:
            res.discard(n)
        return list(res)

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n)-1
            nums[i] = -abs(nums[i])
        return [i+1 for i, n in enumerate(nums) if n > 0]
