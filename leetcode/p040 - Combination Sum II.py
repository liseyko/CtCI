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
        
        def dfs(idxs={i for i in range(len(nums))}, r=[], t=target):
            #print(r)
            if t == 0:
                r.sort()
                if r not in res:
                    res.append(r)
                
            for i in idxs:
                if t - nums[i] < 0:
                    return
                dfs(idxs-{i}, r + [nums[i]], t-nums[i])

        dfs()
        return res