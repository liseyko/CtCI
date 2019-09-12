class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = list(num1), list(num2)
        carry = 0
        res = []
        while l1 or l2 or carry:
            if l1:
                carry += ord(l1.pop())-ord('0')
            if l2:
                carry += ord(l2.pop())-ord('0')
            res.append(chr(carry % 10 + ord('0')))
            carry //= 10
        return ''.join(res[::-1])
