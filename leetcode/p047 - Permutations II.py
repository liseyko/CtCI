class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        def dp(idxs={i for i in range(len(nums))}, r=[]):
            if len(r) == len(nums): 
                res.append(r)
                return

            p = None
            for i in idxs:
                if nums[i] == p: continue
                p = nums[i]
                dp(idxs-{i}, r+[nums[i]])

        dp()
        return(res)
        
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: 
                        break
            ans = new_ans
        return ans   