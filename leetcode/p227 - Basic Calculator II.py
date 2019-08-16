class Solution:
    def calculate(self, s: str) -> int:
        stk, sign, i, op = [], 1, 0, None

        def collectNum(i):
            n = 0
            while i < len(s) and s[i].isnumeric():
                n, i = n * 10 + int(s[i]), i+1
            stk.append(sign*n)
            return i

        while i < len(s):
            c = s[i]
            if c.isnumeric():
                i = collectNum(i)
                if op:
                    b, a = stk.pop(), stk.pop()
                    sign = -1 if a < 0 else 1
                    a = abs(a)
                    stk.append(sign * getattr(operator, op)(a,b))
                    op = None
            else:
                sign = 1
                if c == '*':
                    op = 'mul'
                elif c == '/':
                    op = '__ifloordiv__'
                elif c == '-':
                    sign = -1
                i += 1

        return sum(stk)
