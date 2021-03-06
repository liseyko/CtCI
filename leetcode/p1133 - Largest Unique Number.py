class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A.sort(reverse=True)
        prev = None
        A.append(prev)
        for i, n in enumerate(A[:-1]):
            if  prev != n != A[i+1]:
                return n
            prev = n
        return A[0] if len(A) == 1 else -1

    def largestUniqueNumber(self, A: List[int]) -> int:
        da = collections.Counter(A)
        res = -1
        for k, v in da.items():
            if v == 1 and k > res:
                res = k
        return res
