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
