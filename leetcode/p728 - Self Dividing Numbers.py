class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def chk(i):
            for c in str(i):
                divisor = int(c)
                if not divisor or i % divisor:
                    return False
            return True

        return list(filter(chk, range(left, right + 1)))