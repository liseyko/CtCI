class Solution:
    def calculate(self, s: str) -> int:
        ops = {'-': "sub", '+': "add"}

        def eval(i=0):
            res = 0
            arg = 0
            op = "+"
            while i < len(s) or arg:
                if i < len(s) and "0" <= s[i] <= "9":
                    arg, i = arg*10 + ord(s[i]) - ord('0'), i+1
                elif arg:
                    res = getattr(operator, ops[op])(res, arg)
                    arg = 0
                elif s[i] in ops:
                    op, i = s[i], i+1
                elif s[i] == ')':
                    return res, i+1
                elif s[i] == '(':
                    arg, i = eval(i+1)
                else:
                    i += 1
            return res, i
        return eval()[0]
