class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        i, j = 0, len(nums)-1
        
        res = []
        
        def dfs(idx=0, r=[], t=target):
            #print(r)
            if t == 0:
                res.append(r)
                
            for i in range (idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]: 
                    continue
                if t - nums[i] < 0:
                    return
                dfs(i+1, r + [nums[i]], t-nums[i])

        dfs()
        return res

    """
    def combinationSum2(self, nums, target):
        nums.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())
        for num in nums:
            for t in range(target, num-1, -1):
                for prev in dp[t - num]:
                    print('t-n:', t, num, prev)
                    dp[t].add(prev + (num,))
                    
        return list(dp[-1])
    
    def combinationSum2(self, nums, target):    
        nums.sort()                      
        result = []
        self.combine_sum_2(nums, 0, [], result, target)
        return result
    
    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider 
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return
    
        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                           result, target - nums[i])
    """