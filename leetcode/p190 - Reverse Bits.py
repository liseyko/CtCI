class Solution:
    # @param n, an integer
    # @return an integer
    def __init__(self):
        self.cache = {0:0}

    def reverseBits(self, n):
        
        r = 0
        for _ in range(32):
            r = (r << 1) + (n & 1)
            n >>= 1
        return r

    def reverseByte(self, byte):
        if byte not in self.cache:
            n, r = byte, 0
            for _ in range(8):
                r = (r << 1) + (n & 1)
                n >>= 1
            self.cache[byte] = r
        return self.cache[byte]

    def reverseBits(self, n):
        bytes = [0] * 4
        for i in range(4):
            bytes[i] = n & 255
            n >>= 8
        r = 0
        print(bytes)
        for b in bytes:
            r = (r << 8) + self.reverseByte(b)
        return r
