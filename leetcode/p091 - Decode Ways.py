class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        vis = [0]*len(s)
        mem = [-1]*(len(s))+[1]

        def dfs(i=0):
            if mem[i] > -1:
                return mem[i]
            if s[i] == '0':
                mem[i] = 0
                return 0
            res = dfs(i+1)
            if i < len(s)-1 and (s[i] == '1' or
               s[i] == '2' and s[i+1] < '7'):
                res += dfs(i+2)
            mem[i] = res
            return res

        return dfs() if s else 0
