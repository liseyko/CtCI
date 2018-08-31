class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint = 2**31-1
        #maxint //=10
        #maxint_remainder = 7 
        r = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
            maxint += 1 # or maxint_remainder += 1
        while x != 0:
            #we could check for maxint/10+maxint%10 here instead
            #like: if r > maxint or (r == maxint and x%10 > maxint_remainder):
            r = r*10 + x%10
            if r > maxint:
                return 0
            x //= 10

        return r*sign