class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = - n
            x = 1 / x
        if n % 2:
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)

    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = - n
            x = 1 / x
        r = 1
        while n > 0:
            if n & 1:
                r *= x
            x *= x
            n >>= 1
        return r

    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n *= -1
        ans, current_product = 1, x
        while n > 0:
            if n % 2 == 1:
                ans *= current_product
            current_product *= current_product
            n //= 2
        return ans
