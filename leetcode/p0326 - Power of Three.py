class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1:
            n, rem = divmod(n, 3)
            if rem or not n:
                return False
        return True

    def isPowerOfThree(self, n):
        return n > 0 and not 3**19 % n
