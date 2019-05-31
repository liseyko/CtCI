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
        r = set()
        p = '()'
        if n < 2:
            return [p] if n else ['']
        for sub_r in self.generateParenthesis(n-1):
            for i in range(len(sub_r) + 1):
                r.add(sub_r[:i] + p + sub_r[i:])
        return list(r)
