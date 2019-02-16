class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        if not triangle:
            return 0
        res = float('inf')

        def dfs(lvl=0, i=0, s=0):
            nonlocal res
            if lvl == len(triangle):
                res = min(res, s)
                return
            for j in (i, i+1):
                if -1 < j < len(triangle[lvl]):
                    dfs(lvl+1, j, s+triangle[lvl][j])
        dfs()
        return res

    def minimumTotal(self, t: 'List[List[int]]') -> 'int':
        for lvl in range(len(t)-1, 0, -1):
            for i in range(0, len(t[lvl])-1):
                t[lvl-1][i] += min(t[lvl][i], t[lvl][i+1])
        return t[0][0]

    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        res = triangle[-1] if triangle else [0]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
