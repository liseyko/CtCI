class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expandPal(i, j):
            while 0 < i and j < len(s)-1 and s[i-1] == s[j+1]:
                i, j = i-1, j+1
            return j-i, i, j

        res = (0, 0, 0)
        i = 0
        while i < len(s):
            j = i
            while j+1 < len(s) and s[j+1] == s[i]:
                j += 1
            res = max(res, expandPal(i, j))
            i += (j-i+1)
        return s[res[1]:res[2]+1]

    def longestPalindrome(self, s: str) -> str:

        def expandPalAround(i, j):
            while 0 < i and j < len(s)-1 and s[i-1] == s[j+1]:
                i, j = i-1, j+1
            return j-i, i, j

        def findLastIndexOfAdjacentDupes(i):
            j = i
            while j+1 < len(s) and s[j+1] == s[i]:
                j += 1
            return j

        res = (0, 0, 0)  # palLen, start, end
        i = 0
        while i < len(s):
            j = findLastIndexOfAdjacentDupes(i)
            res = max(res, expandPalAround(i, j))
            i += (j-i+1)
        return s[res[1]:res[2]+1]


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
