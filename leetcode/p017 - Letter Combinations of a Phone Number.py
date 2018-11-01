class Solution:
    def __init__(self):
        self.d2l = {'1': '*', '2': 'abc', '3': 'def', \
                    '4': 'ghi', '5': 'jkl', '6': 'mno', \
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        res = []
        def bt(r=[], i=0):
            if len(r) == len(digits):
                res.append(''.join(r))
                return
            for d in self.d2l[digits[i]]:
                bt(r + [d], i + 1)

        bt()
        return res