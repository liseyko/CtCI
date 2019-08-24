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

    def removeOuterParentheses(self, S: str) -> str:
        cnt, res = 0, []
        for c in S:
            if c == ')':
                cnt -= 1
            if cnt != 0:
                res += [c]
            if c == '(':
                cnt+=1
        return ''.join(res)
