class Solution:
    def isValid(self, s: str) -> bool:
        op = set('([{')
        cl = set(')]}')
        opParOrds = []
        for c in s:
            if c in op:
                opParOrds.append(ord(c))
            elif c in cl and\
                    (not opParOrds or abs(ord(c) - opParOrds.pop()) > 2):
                return False
        return len(opParOrds) == 0
