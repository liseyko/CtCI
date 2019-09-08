class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnts = collections.Counter(s).values()
        oddNumbersAllowed = 1
        for c in cnts:
            if c % 2 == 1:
                if not oddNumbersAllowed:
                    return False
                oddNumbersAllowed = 0
        return True
