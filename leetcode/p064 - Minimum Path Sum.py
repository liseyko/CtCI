class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid[0]), len(grid)
        for j in range(1,n): grid[j][0] += grid[j-1][0]
        for i in range(1,m): grid[0][i] += grid[0][i-1]

        for j in range(1,n):
            for i in range(1,m):
                grid[j][i] += min(grid[j-1][i], grid[j][i-1])

        return grid[-1][-1]