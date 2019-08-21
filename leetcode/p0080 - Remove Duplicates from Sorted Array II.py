class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        j = dupes = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                dupes += 1
            else:
                dupes = 0
            if nums[i] != nums[j] or dupes == 1:
                j += 1
                nums[j] = nums[i]
        j = j+1 if nums else j
        return j

    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        i = 2 if len(nums) > 1 else len(nums)
        for num in nums[2:]:
            if num > nums[i - 2]:
                nums[i], i = num, i+1
        return i
