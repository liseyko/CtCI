class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def spiral(n):
            i = j = loop = 0
            k, n = n ** 2, n - 1
            
            while k > 1:
                while i < n - loop:
                    yield (i, j)
                    i, k = i + 1, k - 1
                while j < n - loop:
                    yield (i, j)
                    j, k = j + 1, k - 1
                while i > loop:
                    yield (i, j)
                    i, k = i - 1, k - 1
                loop += 1                    
                while j > loop:
                    yield (i, j)
                    j, k = j - 1, k - 1
            yield (i, j)
       
        if not n: return []
        grid = [[None for _ in range(n)] for _ in range(n)]
        
        for idx, (i, j) in enumerate(spiral(n)):
            grid[j][i] = idx + 1

        return grid

    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
