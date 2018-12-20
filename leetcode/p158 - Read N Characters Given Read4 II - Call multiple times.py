# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf = [None] * 4
        self.buflen = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if not self.buflen:
                self.buflen = read4(self.buf)
                if not self.buflen:
                    break
            actual_size = min(n - i, self.buflen)
            buf[i:] = self.buf[:actual_size]
            i += actual_size
            
            if actual_size < self.buflen:
                self.buf = self.buf[actual_size:self.buflen]
                self.buflen = len(self.buf)
                for _ in range(self.buflen, 4):
                    self.buf.append(None)
            else:
                self.buflen = 0
            
        return i
    
    def __init__(self):
        self.queue = []
        
    def read(self, buf, n):
        read, need, buffer = 0, n, [None]*4
        while need > 0:
            k = read4(buffer)
            self.queue.extend(buffer[:k])
            need = min(len(self.queue), n - read)
            buf[read:read+need] = [self.queue.pop(0) for _ in xrange(need)]
            read += need
        return read