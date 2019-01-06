class Solution:
    def letterCombinations(self, digits):
        d2l = {'1': '*', '2': 'abc', '3': 'def',
               '4': 'ghi', '5': 'jkl', '6': 'mno',
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}
        res, dl = [], len(digits)
        buf = [0] * dl

        def bt(i=0):
            if digits:
                if i == dl:
                    res.append(''.join(buf))
                    return
                for d in d2l[digits[i]]:
                    buf[i] = d
                    bt(i+1)
        bt()
        return res
