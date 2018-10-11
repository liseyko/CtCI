class Solution:

    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans    

    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = set()      
        p = '()'
        if n < 1: return [""]
        if n == 1:
            return [p]
        for sub_r in self.generateParenthesis(n-1):
            for i in range(len(sub_r) + 1):
                r.add(sub_r[:i] + p + sub_r[i:])
        return list(r)

