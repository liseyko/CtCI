class Solution:
    def calculate(self, s: str) -> int:
        stk, n, op = [], 0, '+'
        for c in s+'+':
            if c.isdigit():
                n = n * 10 + int(c)
            elif c in {'+', '-', '*', '/'}:
                if op == '-':
                    n *= -1
                if op in '-+':
                    stk.append(n)
                elif op == '*':
                    stk[-1] *= n
                elif op == '/':
                    sign = 1 if stk[-1] >= 0 else -1
                    stk[-1] = abs(stk[-1]) // n * sign
                op, n = c, 0

        return sum(stk)
