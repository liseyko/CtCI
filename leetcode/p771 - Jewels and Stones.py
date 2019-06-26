class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        JS = set(J)
        return sum(s in JS for s in S)
