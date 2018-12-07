class Solution:

    
    def subarraySum(self, nums, k):
        if not nums: return 0
        res = 0; l = len(nums)
        
        for i in range(l):
            for j in range(i,l):
                if sum(nums[i:j+1]) == k:
                    res += 1

        return res

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums: return 0
        res = 0; l = len(nums)
        
        sums = {-1 : 0}
        for i in range(l):
            sums[i] = sums[i-1] + nums[i]
            if sums[i] == k:
                res += 1

        for i in range(l):
            for j in range(i+1,l):
                if sums[j] - sums[i] == k:
                    res += 1
        return res