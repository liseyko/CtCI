class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #intmin, intmax = -2**31, 2**31-1
        r, neg, sign = x, False, 1
        if not n: return 1
        if n < 0:
            neg = True
            n = abs(n)
            
        if x < 0 and n % 2 != 0:
            sign = -1
        
        if abs(x) == 1: return abs(x) * sign
        
        while n > 1 and r and float('-inf') < r < float('inf'):
            r *= x
            n -= 1

        if neg: r = 1 / r
        return r