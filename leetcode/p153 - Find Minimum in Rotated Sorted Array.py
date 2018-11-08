class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def div(l=0, r=len(nums)-1):
            if l == r:
                return(nums[l])
            if nums[l] < nums[r]:
                return nums[l]
            m = (r - l) // 2 + l
            if nums[l] < nums[m]:
                return div(m+1, r)
            else:
                return div(l+1, m)

        return div()