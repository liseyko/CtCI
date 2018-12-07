class Solution:
    
    def subarraySum(self, nums, k):
        if not nums: return 0
        res = 0; l = len(nums)
        
        for i in range(l):
            for j in range(i,l):
                if sum(nums[i:j+1]) == k:
                    res += 1
            
        return res    
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums: return 0
        res = 0; l = len(nums)
        
        sums = {-1 : 0}
        for i in range(l):
            sums[i] = sums[i-1] + nums[i]
            if sums[i] == k:
                res += 1

        for i in range(l):
            for j in range(i+1,l):
                if sums[j] - sums[i] == k:
                    res += 1
        return res
    
#Let's remember count[V], the number of previous prefix sums with value V. If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer.

#This is because at time t, A[0] + A[1] + ... + A[t-1] = W, and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V. Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.

    def subarraySum(self, nums, k):
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res    

    def subarraySum(self, nums, k):
        count = collections.defaultdict(int)
        count[0], csum, res = 1, 0, 0
        for v in nums:
            csum += v
            res += count[csum - k]
            count[csum] += 1
        return res

