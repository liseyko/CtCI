class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nl = len(nums)
        if nl < 2:
            return nl
        i = 0
        while i < nl-1 and nums[i] != nums[i+1]:
            i += 1
        for j in range(i+1,nl):
            if nums[i] != nums[j]:
                i += 1                
                nums[i] = nums[j]
        return(i+1)