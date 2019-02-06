class Solution:
    """
        some testcases:
        ---
        "aaca"
        "ab*a*c*a"
        ---
        "acaabbaccbbacaabbbb"
        "a*.*b*.*a*aa*a*"
        ---
        "aaaaabaccbbccababa"
        "a*b*.*c*c*.*.*.*c"
        ---
        "cababbbcbbcbaacbc"
        "b*a*c*a*.*c*.*.*.*a"
        ---
    """
    def __init__(self):
        self.cache = {}

    def isMatch(self, text, pattern):
        # DP top-down solution
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    firstMatch = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*'\
                       and (pattern[j].isalpha() or pattern[j] == '.'):
                        ans = dp(i, j+2) or firstMatch and dp(i+1, j)
                    else:
                        ans = firstMatch and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def isMatch(self, s, p):
        self.cache = {}
        sl, pl = len(s), len(p)

        def _isMatch(si=0, pi=0):
            if pi == pl:
                return si == sl

            if (si, pi) in self.cache:
                return self.cache[(si, pi)]

            firstMatch = si < sl and (p[pi] == '.' or p[pi] == s[si])

            if pl - pi > 1 and p[pi+1] == '*':
                self.cache[(si, pi)] = _isMatch(si, pi+2) or\
                        firstMatch and _isMatch(si+1, pi)
                return self.cache[(si, pi)]
            else:
                self.cache[(si, pi)] = firstMatch and _isMatch(si+1, pi+1)
                return self.cache[(si, pi)]

        return _isMatch()
