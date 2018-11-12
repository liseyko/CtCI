class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i, c in enumerate(s[::-1]):
            sum += 26**i * (ord(c.upper()) - ord('A') + 1)
        
        return sum