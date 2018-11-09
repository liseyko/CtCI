class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0: return 1 / x * self.myPow(1 / x, -(n + 1))
        if n == 0: return 1
        if n == 2: return x * x
        if n % 2 == 0: return self.myPow( self.myPow(x, n / 2), 2)
        else: return x * self.myPow( x, n - 1)

    def myPow(self, x, n):
        if n == 0: return 1
        if n < 0:
            n = - n
            x = 1 / x
        if n % 2:
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)

    def myPow(self, x, n):
        if n == 0: return 1
        if n < 0:
            n = - n
            x = 1 / x
        r = 1
        while n > 0:
            if n & 1: r *= x
            x *= x
            n >>= 1

        return r
