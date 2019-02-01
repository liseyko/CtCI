class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        j = len(nums)-1
        i = j if nums and target > nums[-1] else 0

        while i < j:
            m = i + (j-i) // 2
            if nums[m] > target:
                j = m-1
            elif nums[m] < target:
                i = m+1
            else:
                i = m
                break

        return i+1 if target > nums[i] else i

    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left
