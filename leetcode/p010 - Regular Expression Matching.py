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
    # DP top-down solution
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            #print(i,j)
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*' and (pattern[j].isalpha() or pattern[j] == '.'):
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    # recursive solution + cache
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        if (s, p) in self.cache:
            return self.cache[(s, p)]

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*' and (p[0].isalpha() or p[0] == '.'):
            self.cache[(s, p)] = (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
            return self.cache[(s, p)]
        else:
            self.cache[(s, p)] = first_match and self.isMatch(s[1:], p[1:]) 
            return self.cache[(s, p)]
