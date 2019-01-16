class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens=[], xy_dif=set(), xy_sum=set()):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    # print(p, q, p-q, p+q)
                    dfs(queens+[q], xy_dif | {p-q}, xy_sum | {p+q})
        result = []
        dfs()
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
