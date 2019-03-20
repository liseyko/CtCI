class Solution:
    def numTrees(self, n: int) -> int:
        res = [1, 1] + [0]*(n-1)
        for i in range(2, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]

    def numTrees(self, n):
        """ Catalan number """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
