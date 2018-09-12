class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_limit = pow(2,31)
        int_limit_rem = int_limit % 10
        int_limit //= 10
        
        sl = len(str)
        i = 0
        sign = 1
        n = 0
        while i < sl and str[i]==' ':
            i += 1
        if i == sl:
            return 0

        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        
        while i < sl and str[i] >= '0' and str[i] <= '9':
            d = ord(str[i])-ord('0')
            if n > int_limit or n == int_limit and d >= int_limit_rem - max(sign, 0):
                return sign * int_limit * 10 + sign * int_limit_rem - max(sign ,0)
            n = n * 10 + d

            i += 1

        return sign*n