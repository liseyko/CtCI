class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
            
        for j in range(m):
            for i in range(n):
                if matrix[j][i] == 0:
                    rows.add(j)
                    cols.add(i)

        for j in range(m):
            for i in range(n):
                if i in cols or j in rows:
                    matrix[j][i] = 0
                    
    def setZeroes(self, matrix):
        if not matrix: return
        self.m, self.n = len(matrix), len(matrix[0])

        def zerofy(x,y):
            for j in range(self.m):
                if matrix[j][x] == 0 and j != y:
                    zerofy(x, j)
                matrix[j][x] = None
            for i in range(self.n):
                if matrix[y][i] == 0 and i != x:
                    zerofy(i, y)
                matrix[y][i] = None
        
        for j in range(self.m):
            for i in range(self.n):
                if matrix[j][i] == 0:
                    zerofy(i,j)

        for j in range(self.m):
            for i in range(self.n):
                if matrix[j][i] == None:
                    matrix[j][i] = 0

    def setZeroes(self, matrix):
        if not matrix: return
        self.n, self.m = len(matrix), len(matrix[0])
        row1 = col1 = True

        for j in range(self.n):
            if matrix[j][0] == 0: col1 = False; break
        for i in range(self.m):
            if matrix[0][i] == 0: row1 = False; break

        for j in range(1, self.n):
            for i in range(1, self.m):
                if matrix[j][i] == 0:
                    matrix[0][i] = 0
                    matrix[j][0] = 0
                    
        for j in range(1, self.n):
            if matrix[j][0] == 0:
                matrix[j] = [0] * self.m

        if not col1: matrix[0][0] = 0

        for i in range(self.m):
            if matrix[0][i] == 0:
                for j in range(1, self.n):
                    matrix[j][i] = 0

        if not row1:
            matrix[0] = [0] * self.m

