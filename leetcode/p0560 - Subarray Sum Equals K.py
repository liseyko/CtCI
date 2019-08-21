class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            csum = 0
            for j in range(i, len(nums)):
                csum += nums[j]
                if csum == k:
                    res += 1
        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        """ Let's remember count[V],
            the number of previous prefix sums with value V.
            If our newest prefix sum has value W, and W-V == K,
            then we add count[V] to our answer. This is because at time t,
            A[0] + A[1] + ... + A[t-1] = W, and there are count[V] indices j
            with j < t-1 and A[0] + A[1] + ... + A[j] = V. Thus, there are
            count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.
        """

        cntrs = collections.defaultdict(int)
        cntrs[0] = 1
        csum = res = 0
        for i in range(len(nums)):
            csum += nums[i]
            if csum-k in cntrs:
                res += cntrs[csum-k]
            cntrs[csum] += 1
        return res
