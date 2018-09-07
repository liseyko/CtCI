class Solution:
    def binarySearch(self, nums, target, l, r):
        if r <= l:
            if target > nums[l]:
                return l+1
            return l
        m = (l + r) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.binarySearch(nums, target, m+1, r)
        else:
            return self.binarySearch(nums, target, l, m-1)
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target, 0, len(nums)-1)