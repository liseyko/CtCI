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

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN, INT_MAX = 2**31, 2**31 - 1
        limits = [None, INT_MAX, INT_MIN]
        signs = {'-': -1, '+': 1}

        i = res = 0
        sign, limit = 1, divmod(INT_MAX, 10)
        while i < len(str)-1 and str[i] == ' ':
            i += 1
        if i < len(str)-1 and str[i] in signs:
            sign, limit = signs[str[i]], divmod(limits[signs[str[i]]], 10)
            i += 1

        while i < len(str) and ord('0') <= ord(str[i]) <= ord('9'):
            digit = ord(str[i])-ord('0')
            if res >= limit[0] and res - limit[0] + digit >= limit[1]:
                return sign * limits[sign]
            res = res * 10 + digit
            i += 1

        return sign * res
