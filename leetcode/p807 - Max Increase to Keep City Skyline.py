class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = [max(row) for row in grid]        
        max_col = [max(col) for col in zip(*grid)]
        # fancy:
        return sum(min(max_row[r], max_col[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))    
        # legacy:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += min(max_col[j], max_row[i]) - grid[i][j]
        return result
