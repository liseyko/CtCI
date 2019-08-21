class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j, I, J = 0, 1, len(A)-1, len(A)
        while i < I and j < J:
            if not A[i] % 2:
                i += 2
            elif A[j] % 2:
                j += 2
            else:
                A[i], A[j] = A[j], A[i]
        return A
