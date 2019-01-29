class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sol, n = [], len(nums)
        for i in range(n-2):
            if i and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                cv = (nums[i], nums[j], nums[k])
                cvs = sum(cv)
                if cvs < 0:
                    j += 1
                elif cvs > 0:
                    k -= 1
                else:
                    sol.append(cv)
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j, k = j+1, k-1
        return sol
