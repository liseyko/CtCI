class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nl = len(nums)
        if nl < 2:
            return nl
        i = 1
        while i < nl and nums[i-1] != nums[i]:
            i +=1
        for j in range(i,nl):
            if nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return(i)
