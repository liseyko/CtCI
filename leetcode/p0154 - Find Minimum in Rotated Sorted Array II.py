class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, hgh = 0, len(nums)-1
        while low < hgh and nums[low] >= nums[hgh]:
            mid = low + (hgh-low) // 2
            if nums[mid] < nums[low]:
                hgh = mid
            elif nums[mid] > nums[hgh]:
                low = mid + 1
            else:
                low, hgh = low+1, hgh-1
        return nums[low]

    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i < j and nums[i] >= nums[j]:
            if nums[i] == nums[j]:
                j -= 1
                continue
            m = i + (j-i)//2
            if nums[i] > nums[m]:
                j = m
            else:
                i = m+1
        return nums[i]
