class Solution:
    def moveZeroes(self, nums):
        i = 0
        while i < len(nums) and nums[i] != 0: i += 1
        j = i + 1
        while j < len(nums):
            if nums[j] == 0: j += 1
            else:
                nums[i] = nums[j]
                i, j = i + 1, j + 1
        while i < len(nums):
            nums[i] = 0
            i += 1
