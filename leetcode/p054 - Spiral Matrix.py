class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        n, m = len(matrix[0]), len(matrix)
        if n == 1: return [matrix[i][0] for i in range(len(matrix))]
        nm, r = n * m, []
        moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        i = j = d = loop = 0
        
        
        while len(r) < nm:
            r.append(matrix[j][i])
            i, j = map(sum,zip((i, j), moves[d]))
            if i == n-1 - loop and d == 0 or j == m-1 - loop and d == 1 or \
               i == loop and d == 2 or j == loop and d == 3:
                d  = (d + 1) % 4
            if i == loop and d == 3: loop += 1

        return r


    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans