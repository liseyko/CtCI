"""
Set union A | B
Set intersection A & B
Set subtraction A & ~B
Set negation ALL_BITS ^ A or ~A
Set bit A |= 1 << bit
Clear bit A &= ~(1 << bit)
Test bit (A & 1 << bit) != 0
Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
Remove last bit A&(A-1)
Get all 1-bits ~0
"""
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)