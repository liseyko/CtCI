class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1

        while i < j:
            if not A[i] % 2:
                i += 1
            elif A[j] % 2:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]

        return A