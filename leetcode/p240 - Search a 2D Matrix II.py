class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i, j = 0, len(matrix)-1
        w = len(matrix[0])
        while i < w and j >= 0:
            if matrix[j][i] == target:
                return True
            elif matrix[j][i] < target:
                i += 1
            else:
                j -= 1
        return False
