class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sl, pl = len(s), len(p)

        def dfs(si=0, pi=0):
            #print(f'{si}/{sl}, {pi}/{pl}')
            if si==sl and pi==pl:
                return True
            if si == sl and p[pi] != '*' or pi == pl:
                return False
            if p[pi] == '*':
                while pi < pl-1 and p[pi]==p[pi+1]:
                    pi += 1
                for i in range(si, sl+1):
                    if dfs(i, pi+1):
                        return True
            elif p[pi] == '?' or p[pi] == s[si]:
                return dfs(si+1, pi+1)
            return False
            
        return dfs()

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        transfer = {}
        state = 0

        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1

        accept = state
        state = set([0])
        
        for char in s:
            state = set([transfer.get((at, token)) for at in state for token in [char, '*', '?']])
        
        return accept in state


    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
