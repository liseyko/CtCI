class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # binary search
        
        def _bs(l, r):
            c = (l + r) // 2
            if nums[c] == target:
                return c
            elif l == r: 
                return -1
            elif nums[c] > target:
                return _bs(l, c - 1)
            else:
                return _bs(c + 1, r)

        def bs(l=0, r=len(nums)-1):
            if not nums or target < nums[0] or target > nums[-1]:
                return -1
            return _bs(l,r)

        i = j = bs()
        if i > -1:
            while i > 0 and nums[i - 1] == nums[i]:
                i -= 1
            while j < len(nums) - 1 and nums[j + 1] == nums[j]:
                j += 1

        return [i, j]