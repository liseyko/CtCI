class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        self.m, self.n = len(grid[0]), len(grid)
        
        def chk_tile(i0,j0):
            r = 0
            for i in i0-1, i0+1:
                if i < 0 or i >= self.m or not grid[j0][i]:
                    r += 1
            for j in j0-1, j0+1:
                if j < 0 or j >= self.n or not grid[j][i0]:
                    r += 1
            return r
        
        return sum([chk_tile(i,j) for i in range(self.m) for j in range(self.n) if grid[j][i]])


    def islandPerimeter(self, grid):
        h, w = len(grid), len(grid[0])
        area = 0
        connect = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 1:
                    area += 1
                    # check up and left
                    if r > 0 and grid[r-1][c]: connect += 1
                    if c > 0 and grid[r][c-1]: connect += 1
        return area * 4 - connect * 2