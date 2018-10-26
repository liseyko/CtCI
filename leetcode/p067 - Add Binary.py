class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        maxlen, minlen = len(a), len(b)
        bits, chars = {'0':0, '1':1}, {0:'0', 1:'1'}

        r = list(a)
        leftover = 0
        
        for i in range(maxlen):
            r[~i] = bits[a[~i]] + leftover
            if i < minlen:
                r[~i] += bits[b[~i]]
            elif not leftover:
                r[~i] = chars[r[~i]]
                break
            leftover = r[~i] // 2
            if leftover:
                r[~i] %= 2
            r[~i] = chars[r[~i]]
            
        leftover = ["1" for _ in range(leftover)]
        return ''.join(leftover + r)