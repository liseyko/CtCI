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

    def calculate(self, s):
        ops = set(['-', '+'])
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c in ops:
                res += sign*num
                num = 0
                sign = [-1, 1][c == "+"]
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign
