class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nl = len(nums)
        nums.sort()
        res = []
        if nl < 4 or target > sum(nums[-4:]): 
            return res
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if sum(nums[i:i+4]) > target:
                break
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if sum(nums[j:j+3]) > target-nums[i]:
                    break
                k, m = j+1, len(nums)-1
                t = target - nums[i] - nums[j]
                while k < m:
                    km = nums[k]+nums[m]
                    if km < t:
                        k += 1
                    elif km > t:
                        m -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        k, m = k+1, m-1
                        while k < m and nums[k] == nums[k-1]: 
                            k += 1
        return res


    """
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
        """
