class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        # recursive with memorization
        mem = [-1]*(len(s))+[1]

        def dfs(i=0):
            if mem[i] > -1:
                return mem[i]
            if s[i] == '0':
                mem[i] = 0
                return 0
            res = dfs(i+1)
            if i < len(s)-1 and (s[i] == '1'
               or s[i] == '2' and s[i+1] < '7'):
                res += dfs(i+2)
            mem[i] = res
            return res

        return dfs() if s else 0

    def numDecodings(self, s: 'str') -> 'int':
        # dp + O(n) space
        dp = [0]*(len(s))+[1]

        for i in range(len(s)-1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
            if i < len(s)-1 and (s[i] == '1'
               or s[i] == '2' and s[i+1] < '7'):
                dp[i] += dp[i+2]

        return dp[0] if s else 0

    def numDecodings(self, s: 'str') -> 'int':
        # dp + O(1) space
        dp = [0, 1, 0]

        for i in range(len(s)-1, -1, -1):
            if s[i] != '0':
                dp[0] = dp[1]
            if i < len(s)-1 and (s[i] == '1'
               or s[i] == '2' and s[i+1] < '7'):
                dp[0] += dp[2]
            dp[:] = 0, *dp[:2]

        return dp[1] if s else 0
