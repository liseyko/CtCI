class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = currentSum = nums[0] if nums else None
        for i in range(1, len(nums)):
            n = nums[i]
            currentSum = max(currentSum + n, n)
            result = max(result, currentSum)
        return result
    
    def maximumSum(self, nums: List[int]) -> int:
        negNumIdxs = [i for i, n in enumerate(nums) if n < 0]
        #print(negNumIdxs)
        if not negNumIdxs or len(nums)<2:
            res = self.maxSubArray(nums)
        else:
            res = float('-inf')
            for i in negNumIdxs:
                #print(nums[:i]+nums[i+1:])
                subres = self.maxSubArray(nums[:i]+nums[i+1:])
                res = max(res, subres)
        return res
