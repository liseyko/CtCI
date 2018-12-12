class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = 0
        while x or y:
            if x & 1 != y & 1:
                r += 1
            x >>= 1
            y >>= 1
            
        return r

    def hammingDistance(self, x, y):
        return sum(1 for x in (bin(x^y)[2:]) if x == '1')