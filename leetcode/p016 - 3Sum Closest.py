class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return None

        res = float('inf')
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l +=1 
                elif s > target:
                    r -= 1
                else:
                    return target

        return res