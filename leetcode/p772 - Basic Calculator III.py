class Solution:
    def calculate(self, s: str, i=0) -> int:
        stk, n, op = [], 0, '+'

        while i <= len(s):
            c = s[i] if i < len(s) else '\n'
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == '(':
                n, i = self.calculate(s, i+1)
            elif c in {'+', '-', '*', '/', ')', '\n'}:
                if op == '-':
                    n *= -1
                if op in '-+':
                    stk.append(n)
                elif op == '*':
                    stk[-1] *= n
                elif op == '/':
                    sign = 1 if stk[-1] >= 0 else -1
                    stk[-1] = abs(stk[-1]) // n * sign
                if c == ')':
                    return sum(stk), i
                op, n = c, 0
            i += 1

        return sum(stk)
