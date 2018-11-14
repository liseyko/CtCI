class Solution:
    
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        ABCD = A×26³ + B×26² + C×26¹ + D = 1×26³ + 2×26² + 3×26¹ + 4
        We can't simply use the n%26 method because:
        ZZZZ = Z×26³+Z×26²+Z×26¹+Z = 26+26³+26×26²+26×26¹+26
        We can use (n-1)%26 instead, then we get a number range from 0 to 25.
        """
        r = []
        
        while n > 0:
            r.append(chr(ord('A') + (n-1) % 26))
            n = (n-1) // 26
        
        return(''.join(r[::-1]))