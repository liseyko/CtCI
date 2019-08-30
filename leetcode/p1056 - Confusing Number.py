class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated = [0,1,None,None,None,None,9,None,8,6]
        ncopy, n180 = n, 0
        while ncopy:
            ncopy, digit = divmod(ncopy, 10)
            if rotated[digit] is None:
                return False
            n180 = n180 * 10 + rotated[digit]
        return n != n180
