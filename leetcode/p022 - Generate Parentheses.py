class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(s="", lc=0, rc=0):
            if len(s) == 2*n:
                res.append(s)
                return
            if lc < n:
                bt(s+"(", lc+1, rc)
            if rc < lc:
                bt(s+")", lc, rc+1)
        bt()
        return res

    def generateParenthesis(self, n):
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans if n else ['']

    def generateParenthesis(self, n):
        res = set()
        p = '()'
        if n < 2:
            return [p] if n else ['']
        for subres in self.generateParenthesis(n-1):
            for i in range(len(subres) + 1):
                res.add(subres[:i] + p + subres[i:])
        return list(res)
