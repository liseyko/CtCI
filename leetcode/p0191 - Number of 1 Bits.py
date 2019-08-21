class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingWeight(self, n):
        r = 0
        while n:
            r += n & 1
            n >>= 1
        return r
