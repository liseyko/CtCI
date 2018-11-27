class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        
        m, n = len(grid[0]), len(grid)
        
        def removeIsland(j,i):
            grid[j][i] = '0'
            for i0 in i-1, i+1:
                if 0 <= i0 < m and grid[j][i0] == '1':
                    removeIsland(j,i0)
            for j0 in j-1, j+1:
                if 0 <= j0 < n and grid[j0][i] == '1':
                    removeIsland(j0,i)
        
        res = 0
        for j in range(n):
            for i in range(m):
                if grid[j][i] == '1':
                    res += 1
                    removeIsland(j,i)

        return res