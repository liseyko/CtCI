class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        n2 = len(matrix) // 2 + len(matrix) % 2
        
        for j in range(n2):
            for i in range(j, n-j):
                matrix[j][i], matrix[i][n-j], matrix[n-j][n-i], matrix[n-i][j] = \
                matrix[n-i][j], matrix[j][i], matrix[i][n-j], matrix[n-j][n-i]

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

    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                for _ in '123':
                    A[i][j], A[~j][i], i, j = A[~j][i], A[i][j], ~j, ~i
                i = ~j