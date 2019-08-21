class Solution:
    
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))    

    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans    
            
    def maxAreaOfIsland(self, grid):
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
