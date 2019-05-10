class Solution:
    def reverse(self, x: int) -> int:
        intLimits = {-1: 2**31, 1: 2**31-1}
        sign = -1 if x < 0 else 1
        softLimit, hardLimit = divmod(intLimits[sign], 10)
        x *= sign
        rx = 0
        while x:
            if rx > softLimit or rx == softLimit and x > hardLimit:
                return 0
            rx = rx * 10 + x % 10
            x //= 10

        return sign * rx
