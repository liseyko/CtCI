class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n, i = 2, 0
        while n < x:
            n <<= 1
            i += 1
            
        n0 = 2 ** (i // 2)  

        while True:
            n1 = ( n0 + x / n0 ) / 2
            if int(n1) == int(n0):
                return int(n1)
            n0 = n1

    def mySqrt(self, x):
        res = 0
        bit = 1 << 30
 
        while bit > x:
            bit >>= 2
        
        while bit != 0:
            if x >= res + bit:
                x -= res + bit
                res += bit << 1
                
            res >>= 1
            bit >>= 2

        return res