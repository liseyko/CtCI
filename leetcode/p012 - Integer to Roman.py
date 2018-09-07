class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i2r = {1000:'M', 900:'CM', 500:'D', 400:'CD', \
                100:'C', 90: 'XC', 50: 'L', 40: 'XL', \
                 10:'X', 9:  'IX', 5:  'V', 4:  'IV', 1: 'I'}
        r = []
        for i in ints:
            while num >= i:
                num -= i
                r.append(i2r[i])
            if num == 0:
                break
                
        return ''.join(r)