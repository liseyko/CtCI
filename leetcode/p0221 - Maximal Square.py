class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        prevRowSq = [0] * (len(matrix[0]) if matrix else 0 + 1)
        maxSq = 0
        for row in matrix:
            curRowSq = [0] * (len(row)+1)
            for i in range(len(row)):
                if row[i] == '1':
                    curRowSq[i] = min(curRowSq[i-1], prevRowSq[i-1], prevRowSq[i])+1
                    maxSq = max(maxSq, curRowSq[i])
            prevRowSq = curRowSq
        return maxSq**2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        prevRowSq = [0] * (len(matrix[0]) if matrix else 0 + 1)
        maxSq = 0

        def updCurSq(i, curRowSq):
            nonlocal prevRowSq, maxSq
            curRowSq[i] = min(curRowSq[i-1], prevRowSq[i-1], prevRowSq[i])+1
            maxSq = max(maxSq, curRowSq[i])

        def updSqrsInRow(row):
            nonlocal prevRowSq
            curRowSq = [0] * (len(row)+1)
            for i in range(len(row)):
                if row[i] == '1':
                    updCurSq(i, curRowSq)
            prevRowSq = curRowSq

        for row in matrix:
            updSqrsInRow(row)

        return maxSq**2


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
