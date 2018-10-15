class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2: return True
        i, j = 0, len(s)-1
        m = j // 2

        while i < j and i <= m and j >= m:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i, j = i+1, j-1

        return True