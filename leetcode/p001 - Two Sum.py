class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxs = {}
        
        for i, n in enumerate(nums):
            if tgt - n in idxs:
                return [idxs[tgt-n], i]
            idxs[n] = i