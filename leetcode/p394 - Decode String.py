class Solution:
    def decodeString(self, s: str) -> str:
        res, stk, cntr, i = [], [], 0, 0
        for c in s:
            if c.isdigit():
                cntr = cntr * 10 + int(c)
            elif c == '[':
                stk.extend([res, cntr])
                res, cntr = [], 0
            elif c == ']':
                res *= stk.pop()
                res = stk.pop() + res
            else:
                res.append(c)
        return ''.join(res)

    def decodeString(self, s: str) -> str:
        res, buf, cntr, i = [], [], 0, 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                cntr = cntr * 10 + int(c)
            elif c.isalpha():
                buf.append(c)
            elif c == '[':
                res.extend(buf)
                j = i = i+1
                op = 1
                while s[i] != ']' or op != 1:
                    if s[i] == '[':
                        op += 1
                    elif s[i] == ']':
                        op -= 1
                    i += 1
                buf = self.decodeString(s[j:i])
                for _ in range(cntr):
                    res.extend(buf)
                cntr, buf = 0, []
            i += 1
        res.extend(buf)
        return ''.join(res)

