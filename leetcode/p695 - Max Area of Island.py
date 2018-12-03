class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        self.m, self.n = len(grid[0]), len(grid)
        res = 0

        def dfs(j0, i0):
            grid[j0][i0], area = 0, 1
            for j in j0 - 1, j0 + 1:
                if -1 < j < self.n and grid[j][i0]:
                    area += dfs(j, i0)
            for i in i0 - 1, i0 + 1:
                if -1 < i < self.m and grid[j0][i]:
                    area += dfs(j0, i)
            return area

        for j in range(self.n):
            for i in range(self.m):
                if grid[j][i]:
                    res = max(res, dfs(j, i))

        return res
