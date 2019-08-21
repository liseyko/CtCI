class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = x ^ y, 0
        while x:
            y += x & 1
            x >>=1
            
        return y

    def hammingDistance(self, x, y):
        return bin(x^y)[2:].count('1')

