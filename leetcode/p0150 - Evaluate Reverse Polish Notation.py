class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {
               '+': 'add',
               '-': 'sub',
               '*': 'mul',
               '/': 'truediv',
              }
        for t in tokens:
            if t in ops:
                n = stk.pop()
                stk[-1] = int(getattr(operator, ops[t])(stk[-1], n))
            else:
                stk.append(int(t))
        return stk[-1]
