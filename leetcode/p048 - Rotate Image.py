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