class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -9e9
        nums.sort()
        #print(nums)
        for i in range(len(nums)-1):
            if sum(nums[i:i+2]) >= k:
                break
            j = bisect.bisect_left(nums, k-nums[i], i+1, len(nums))-1
            #print(i,j, nums[i], nums[j], nums[i]+nums[j])
            res = max(res, nums[i]+nums[j])
            if res == k-1:
                break
        return res if res != -9e9 else -1

    def twoSumLessThanK(self, nums: List[int], k: int) -> int:    
        nums.sort()   
        i, j = 0, len(nums)-1
        res = -9e9
        while i < j:
            summ = nums[i] + nums[j]
            if summ < k:  # found one candidate
                res = max(res, summ)
                i += 1
            else:
                j -= 1
        return res if res != -9e9 else -1

