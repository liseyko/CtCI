# TODO: abs(dividend) is wrong. what if divident == INT_MIN
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -1 << 31, 1 << 31 - 1
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        if not dividend or dividend < divisor: return 0
        
        r = 0
        while dividend >= divisor:
            for i in range(32):
                if (divisor << i + 1) > dividend:
                    break
            print(r, 1 << i)
            r += 1 << i
            if r == 2147483648 and not negative: return r - 1            
            dividend -= divisor << i
            
        if negative:
            r = ~r + 1
        return r