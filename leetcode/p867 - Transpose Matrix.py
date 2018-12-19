class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]: return A

        ln = min(len(A), len(A[0]))
        for j in range(ln):
            for i in range(j):
                    A[j][i], A[i][j] = A[i][j], A[j][i]

        if len(A) < len(A[0]):
            for i in range(ln, len(A[0])):
                A.append([])
                for j in range(ln):
                    A[-1].append(A[j][i])
                
            for j in range(ln):
                A[j] = A[j][:ln]
                
        elif len(A) > len(A[0]):
            for i in range(len(A[0])):
                for j in range(ln, len(A)):
                    A[i].append(A[j][i])
            A = A[:ln]
        return A

    def transpose(self, A):
        return zip(*A)

    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans