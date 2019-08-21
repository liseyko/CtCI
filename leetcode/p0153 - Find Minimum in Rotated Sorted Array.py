class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bs(i=0, j=len(nums)-1):
            if i == j or nums[i] < nums[j]:
                return nums[i]
            m = i + (j-i) // 2
            if nums[m] < nums[i]:
                return bs(i, m)
            else:
                return bs(m+1, j)

        if nums:
            return bs()
