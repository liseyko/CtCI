class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #if not nums or len(nums) < 2: return nums
        res = [1, nums[0]]
        for i in range(1, len(nums)-1):
            res.append(res[-1] * nums[i])
        print(res) 
        
        subres = nums[-1]
        for i in range(1,len(nums)):
            res[~i] *= subres
            subres *= nums[~i]
        return res