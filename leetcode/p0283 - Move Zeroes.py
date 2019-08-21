class Solution:
    def moveZeroes(self, nums):
        offset = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                offset += 1
            elif offset > 0:
                nums[i - offset], nums[i] = nums[i], 0

    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
