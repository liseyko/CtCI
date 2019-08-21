class Solution:

    def chk_pal(self, s, lr):
        l, r = lr
        while l > 0 and r < len(s)-1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
        return l, r

    def upd_max(self, lr):
        l, r = lr
        if r - l + 1 > self.max_pal[0]:
            self.max_pal = r-l+1, (l, r)

    def findSame(self, s, i):
        j = i
        while j < len(s)-1 and s[j+1] == s[i]:
            j += 1
            self.i = j
        return i, j

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        self.i, self.max_pal = 0, (1, (0, 0))
        while self.i < len(s)-1:
            self.upd_max(self.chk_pal(s, self.findSame(s, self.i)))
            self.i += 1

        return s[self.max_pal[1][0]:self.max_pal[1][1]+1]


class Solution:
    """
    Manacher algorithm
    http://en.wikipedia.org/wiki/Longest_palindromic_substring
    """
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^a#b#b#a$".
        # ^ and $ signs are added to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i])  # = i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('021012101'))
    print(sol.longestPalindrome('rfkqyuqfjkxy'))
    print(sol.longestPalindrome('bb'))
    print(sol.longestPalindrome('bbb'))
    print(sol.longestPalindrome('cbbd'))
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('abracadabrarbd'))
    print(sol.longestPalindrome('"3210123210012321001232100123210012321001232\
1001232100123210012321001232100123210012321001232100123210012321001232100\
1232100123210012321001232100123210012321001232100123210012321012321001232\
1001232100123210012321001232100123210012321001232100123210012321001232100\
1232100123210012321001232100123210012321001232100123210012321001232100123\
2100123210012321001232100123210012321001232100123210012321001232100123210\
0123210012321001232100123210012321001232100123210012321001232100123210012\
3210012321001232100123210012321001232100123210012321001232100123210012321\
0012321001232100123210012321001232100123210012321001232100123210012321001\
2321001232100123210012321001232100123210012321001232100123210012321001232\
1001232100123210012321001232100123210012321001232100123210012321001232100\
1232100123210012321001232100123210012321001232100123210012321001232100123\
2100123210012321001232100123210012321001232100123210012321001232100123210\
0123210012321001232100123210012321001232100123210123210012321001232100123\
210123"'))
