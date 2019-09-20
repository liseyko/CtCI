class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s.replace('abc', ''):
            if c == 'c' and stk[-2:] == ['a', 'b']:
                del stk[-2:]
            else:
                stk.append(c)
        return s and len(stk) == 0
