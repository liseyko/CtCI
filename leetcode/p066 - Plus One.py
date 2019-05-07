class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i, d in enumerate(digits[::-1]):
            carry, digits[~i] = divmod(digits[~i] + carry, 10)
        if carry:
            digits = [carry] + digits

        return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        curDigitIdx = len(digits) - 1
        remainder = 1

        while remainder and curDigitIdx > -1:
            digits[curDigitIdx] += remainder
            remainder, digits[curDigitIdx] = divmod(digits[curDigitIdx], 10)
            curDigitIdx -= 1

        if remainder:
            digits = [remainder] + digits

        return digits
