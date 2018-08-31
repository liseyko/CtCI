class Solution:
    def __init__(self):
        self.max_pal = None
        self.i = 0

    def chk_pal(self, s, ij):
        l, r = ij
        #print('chk:',l,r)
        ln = len(s)
        while l > 0 and r < ln-1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
        #print('chkret:',l,r)
        return l, r

    def upd_max(self,lr):
        l, r = lr
        if r - l + 1 > self.max_pal[0]:
            self.max_pal = r-l+1,(l,r)

    def findSame(self,s,i):
        #l, r, ln = i, i, len(s)
        j, ln = i, len(s)
        #while l > 0 and s[l-1] == s[i]:
        #    l -= 1
        while j < ln-1 and s[j+1] == s[i]:
            j += 1
            self.i = j
        return i, j

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ln = len(s)
        if ln < 2:
            return s

        self.max_pal = 1,(0,0)

        self.i = 0
        while self.i < ln-1:
            self.upd_max(self.chk_pal(s,self.findSame(s,self.i)))
            self.i += 1

        return s[self.max_pal[1][0]:self.max_pal[1][1]+1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('021012101'))
    print(sol.longestPalindrome('rfkqyuqfjkxy'))
    print(sol.longestPalindrome('bb'))
    print(sol.longestPalindrome('bbb'))
    print(sol.longestPalindrome('cbbd'))
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('abracadabrarbd'))
    print(sol.longestPalindrome('"321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"'))

