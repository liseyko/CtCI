class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A) < 2: return 0

        res = 0
        for col in range(len(A[0])):
            for row in range(1, len(A)):
                if ord(A[row - 1][col]) > ord(A[row][col]):
                    res += 1
                    break
        return res

    def minDeletionSize(self, A):
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
        return ans