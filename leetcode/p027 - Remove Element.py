class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        if j < 0 or j == 0 and nums[0] == val:
            return 0
        
        while i <= j:
            if nums[j] == val:
                j -= 1
            elif nums[i] != val:
                i += 1
            else:
                nums[i] = nums[j]
                i, j = i + 1, j - 1
        return j + 1