class Solution:

    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        res = []
        cur_res = [None]*k

        def dfs(i=0, j=0):
            for j in range(j, n):
                cur_res[i] = j+1
                if i == k-1:
                    res.append(cur_res[:])
                else:
                    dfs(i+1, j+1)
        dfs()
        return res

    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        if k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [[i for i in range(1, n+1)]]
        res = self.combine(n-1, k)
        part = self.combine(n-1, k-1)
        for p in part:
            res.append(p + [n])
        return res
