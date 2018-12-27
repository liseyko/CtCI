class Solution:
    def isPalindrome(self, s):
        if len(s) < 2:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i, j = i + 1, j - 1
        return True
