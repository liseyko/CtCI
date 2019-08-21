class Solution:

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(A), 0, -1):
            n = max(A[:i])
            if A[i-1] != n:
                j = A.index(n) + 1
                res.append(j)
                A[:j] = A[:j][::-1]
                print(A)
                res.append(i)
                A[:i] = A[:i][::-1]
                print(A)
        return res

    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res

    def pancakeSort(self, A):
        ans = []
        N = len(A)
        B = sorted(range(1, N+1), key=lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1
        return ans
