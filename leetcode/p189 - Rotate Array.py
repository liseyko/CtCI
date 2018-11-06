class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        def rev(i=0, j=len(nums)-1):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        rev()
        rev(j=k-1)
        rev(k)


        """
        #TODO: cyclic
        for n in range(len(nums) // k - (len(nums) % k == 0)):
            for i in range(k):
                nums[n * k + i], nums[-k + i] = nums[-k + i], nums[n * k + i]
                print(n * k + i, -k + i)
            print(nums)
        print(nums)
        if k > len(nums) // 2:
            for i in range((len(nums) - k) - 1):
                nums[k + i], nums[-1] = nums[-1], nums[k + i]
        """
