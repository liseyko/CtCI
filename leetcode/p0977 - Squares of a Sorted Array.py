class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        i, j = 0, len(A)-1
        while i <= j:
            if A[i] < 0 and -1 * A[i] > A[j]:
                res.append(A[i]**2)
                i += 1
            else:
                res.append(A[j]**2)
                j -= 1
        return res[::-1]

    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        pr = bisect.bisect_left(A, 0)
        pl = pr-1
        while -1 < pl and pr < len(A):
            if A[pr] < A[pl]*(-1):
                res.append(A[pr]**2)
                pr += 1
            else:
                res.append(A[pl]**2)
                pl -= 1
        for pl in range(pl, -1, -1):
            res.append(A[pl]**2)
        for pr in range(pr, len(A)):
            res.append(A[pr]**2)
        return res
