class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPal(i=0, j=len(s)-1, r=1):
            while i < j:
                if s[i] == s[j]:
                    i, j = i+1, j-1
                elif not r:
                    return False
                else:
                    return isPal(i+1, j, r-1) or isPal(i, j-1, r-1)
            return True

        return isPal()

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2+1):
            if s[i] != s[~i]:
                return s[i+1:n-i] == s[i+1:n-i][::-1] or\
                    s[i:~i] == s[i:~i][::-1]
        return True
