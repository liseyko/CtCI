class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, n in enumerate(A):
            if i == n:
                return i
        return -1

    def fixedPoint(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            m = (i + j) // 2
            if A[m] - m < 0:
                i = m + 1
            else:
                j = m
        return i if A[i] == i else -1
