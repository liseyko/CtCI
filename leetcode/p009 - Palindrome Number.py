class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        y = 0
        while x > y:
            y, x = y * 10 + x % 10, x // 10
            print(x,y)

        return x == y or x == y // 10
