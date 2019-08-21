class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, stk = 0, [-1]
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                stk.pop()
                if stk:
                    res = max(res, i - stk[-1])
                else:
                    stk.append(i)
        return res
