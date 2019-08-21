class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        nums.sort()
        return nums[len(nums)//2]