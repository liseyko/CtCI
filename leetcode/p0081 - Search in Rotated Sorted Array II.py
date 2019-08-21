class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == nums[j] != target:
                i, j = i+1, j-1
                continue
            m = i + (j - i) // 2
            if nums[m] == target:
                return True
            elif nums[i] <= nums[m]:
                if nums[i] <= target < nums[m]:
                    j = m-1
                else:
                    i = m+1
            else:
                if nums[m] < target <= nums[j]:
                    i = m+1
                else:
                    j = m-1

        return False
