class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v, nums[k] = nums[k], 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1

    def sortColors(self, nums):
        cntr = [0]*3
        for n in nums:
            cntr[n] += 1
        j = 0
        for i in range(len(nums)):
            while not cntr[j]:
                j += 1
            nums[i] = j
            cntr[j] -= 1
