class Solution:
    
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])
    
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
            
        return ''.join(s)
    
    def reverseString(self, s):
        return s[::-1]