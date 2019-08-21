class Solution:
    
    def maxWidthRamp(self, A):
        #TODO: 
        # idea: Binary Search Candidates
        N = len(A)

        ans = 0
        candidates = [(A[N-1], N-1)]
        # candidates: i's decreasing, by increasing value of A[i]
        for i in range(N-2, -1, -1):
            # Find largest j in candidates with A[j] >= A[i]
            jx = bisect.bisect(candidates, (A[i],))
            if jx < len(candidates):
                ans = max(ans, candidates[jx][1] - i)
            else:
                candidates.append((A[i], i))

        return ans    

    def maxWidthRamp(self, A):
        ans, m = 0, len(A)
        #print(sorted(range(len(A)), key = A.__getitem__))
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        res, miN, idx = 0, len(A)-1, {}
                 
        for i, n  in enumerate(A):
            if n not in idx:
                idx[n] = [i, i]
            else:
                idx[n][1] = i
        
        for n in sorted(idx.keys()):
            miN = min(miN, idx[n][0])
            res = max(res, idx[n][1] - miN)

        return res
