class Solution:

    def moveZeroes(self, nums):
        i = 0

        while i < len(nums) and nums[i] != 0: i += 1
        
        for j in range(i+1, len(nums)):
            if nums[j] != 0:
                nums[i], i = nums[j], i + 1
                
        while i < len(nums):
            nums[i], i = 0, i + 1

    def moveZeroes(self, nums):
        offset = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                offset += 1
            elif offset > 0:
                nums[i - offset], nums[i] = nums[i], 0
