class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        h, w = len(matrix), len(matrix[0])
        i, j = 0, h*w-1
        while i <= j:
            m = i + (j - i) // 2
            col, row = divmod(m, w)
            if matrix[col][row] < target:
                i = m+1
            elif matrix[col][row] > target:
                j = m-1
            else:
                return True
        return False
