# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            c = l + (r - l) // 2
            if isBadVersion(c):
                r = c - 1
            else:
                l = c + 1
        return l
