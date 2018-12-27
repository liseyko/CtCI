class Solution:
    def reverse(self, x):
        limits = [0, 2**31 - 1, 2**31]
        sign = -1 if x < 0 else 1
        limit = divmod(limits[sign], 10)
        r, x = 0, abs(x)
        r = 0
        while x:
            x, digit = divmod(x, 10)
            if r >= limit[0] and (r - limit[0]) * 10 + digit >= limit[1]:
                return 0
            r = r * 10 + digit
        return sign * r
