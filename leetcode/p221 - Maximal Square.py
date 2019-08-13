class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        curMax = wi = hi = 0
        h, w = len(matrix), len(matrix[0]) if matrix else 0

        def checkSquareSize(hi, wi):
            size = 0
            while hi+size < h and wi+size < w:
                for i in range(wi, wi+size+1):
                    if matrix[hi+size][i] != '1':
                        return size
                for i in range(hi, hi+size):
                    if matrix[i][wi+size] != '1':
                        return size
                size += 1
            return size

        while hi < h - curMax:
            while wi < w - curMax:
                if matrix[hi][wi] == "1":
                    curSquareSize = checkSquareSize(hi, wi)
                    curMax = max(curMax, curSquareSize)
                wi += 1
            hi, wi = hi+1, 0
        return curMax**2
