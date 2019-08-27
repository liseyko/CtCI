class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        s = sum([int(c) for c in str(min(A))])
        return int(s % 2 == 0)
