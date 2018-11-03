class Solution:

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxans = 0
        stack = [-1]

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])

        return maxans
