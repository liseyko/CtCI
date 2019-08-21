class Solution:
    def generateParenthesis(self, n):
        res = []

        def bt(lc=0, rc=0, buf=[]):
            if lc == rc == n:
                res.append(''.join(buf))
                return
            if lc < n:
                bt(lc+1, rc, buf+['('])
            if rc < lc:
                bt(lc, rc+1, buf+[')'])
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
