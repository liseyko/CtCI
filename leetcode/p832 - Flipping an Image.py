class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A: return A
        W = len(A[0])
        for row in A:
            i, j = 0, W - 1
            while i < j:
                row[i], row[j] = 1 - row[j], 1 - row[i]
                i, j = i + 1, j - 1
            if i == j:
                row[i] = 1 - row[i]
        return A

    def flipAndInvertImage(self, A):
        return [[i ^ 1 for i in row[::-1]] for row in A]