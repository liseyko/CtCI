class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_mark(j, i):
            if -1 < j < len(grid) and\
               -1 < i < len(grid[0]) and\
               grid[j][i] == '1':
                grid[j][i] = '2'
                for jj in (j-1, j+1):
                    dfs_mark(jj, i)
                for ii in (i-1, i+1):
                    dfs_mark(j, ii)

        res = 0
        for j, row in enumerate(grid):
            for i, area in enumerate(row):
                if area == '1':
                    res += 1
                    dfs_mark(j, i)
        return res
