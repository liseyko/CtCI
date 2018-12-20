# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
  
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i, buf4 = 0, [None] * 4
        while i < n:
            buf4len = min(n - i, read4(buf4))
            if not buf4len: break
            buf[i:] = buf4[:buf4len]
            i += buf4len

        return i