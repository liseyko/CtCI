class Solution:
    def rotate(self, A):
        """
        :type A: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for j in range(len(A)//2):
            for i in range(j,len(A)-1-j):
                A[i][~j], A[~j][~i], A[~i][j], A[j][i] = \
                A[j][i], A[i][~j], A[~j][~i], A[~i][j]

    def rotate(self, A):
        A[:] = map(list, zip(*A[::-1]))

    def rotate(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]

    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]

    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]
