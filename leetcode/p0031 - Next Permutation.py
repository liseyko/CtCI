class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return

        def invert(j):
            for i in range((len(nums) - j) // 2):
                nums[j+i], nums[-i-1] = nums[-i-1], nums[j+i]

        i = len(nums)-2
        while i > -1 and nums[i] >= nums[i+1]: 
            i -= 1
        invert(i+1)
        if i > -1:
            j = i + 1
            while nums[j] <= nums[i]: 
                j += 1
            nums[i], nums[j] = nums[j], nums[i]

