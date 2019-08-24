class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        r, buf, cntr = [], [], 0
        for p in S:
            if p == '(':
                cntr += 1
                buf += ['(']
            elif p == ')':
                cntr -= 1
                buf += [')']
                if not cntr:
                    r.extend(buf[1:-1])
                    buf.clear()
        return ''.join(r)
