class Solution:
    def isPalindrome(self, x):
        if x < 0 or x > 0 and x % 10 == 0:
            return False
        xrev = 0
        while x > xrev:
            xrev = xrev * 10 + x % 10
            x //= 10
        return x == xrev or x == xrev // 10
