class Solution:
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
            state = set([transfer.get((at, token))
                        for at in state for token in [char, '*', '?']])

        return accept in state

    def isMatch(self, s, p):
        si = pi = 0
        ssi = spi = None  # '*' indexes
        sl, pl = len(s), len(p)
        while si < sl:
            if pi < pl and p[pi] == '*':
                ssi, spi = si+1, pi+1
                pi += 1
            elif pi < pl and (p[pi] == s[si] or p[pi] == '?'):
                si, pi = si+1, pi+1
            elif spi is not None:
                si, pi = ssi, spi
                ssi += 1
            else:
                return False

        while pi < pl and p[pi] == '*':
            pi += 1

        return pi == pl
