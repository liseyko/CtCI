class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotatable_digits  = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        ncopy, n180 = n, 0
        while ncopy:
            ncopy, digit = divmod(ncopy, 10)
            if digit not in rotatable_digits:
                return False
            n180 = n180 * 10 + rotatable_digits[digit]
        return n != n180
