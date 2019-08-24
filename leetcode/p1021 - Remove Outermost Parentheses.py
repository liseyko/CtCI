class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        r, buf1, buf2 = [], [], []
        for p in S:
            if p == '(':
                buf1.append('(')
                buf2.append('(')
            elif p == ')':
                buf1.pop()
                buf2.append(')')
                if not buf1:
                    r.extend(buf2[1:-1])
                    buf2.clear()
        return ''.join(r)
