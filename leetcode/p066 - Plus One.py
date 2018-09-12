class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r = 0
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += r
            r = digits[i] // 10
            if r == 0:
                return digits
            else:
                digits[i] %= 10
        
        return [r] + digits