class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return True

        i = len(nums) - 1
        if nums[i] == 0: i -= 1
            
        gap = 0
        while i > -1:
            while i > -1 and gap == 0 and nums[i] != 0: i -= 1
            while i > -1 and (nums[i] == 0 or gap > 0 and nums[i] <= gap): 
                gap, i = gap + 1, i - 1
            if i > -1 and nums[i] > gap:
                gap, i = 0, i - 1
                
        if gap > 0: return False
        
        return True
        
    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
                
        return lastPos == 0