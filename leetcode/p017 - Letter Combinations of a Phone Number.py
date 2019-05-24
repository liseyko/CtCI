class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2c = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z'],
               }

        res, buf = [], [None] * len(digits)

        def convert(di=0):
            if di == len(digits):
                res.append(''.join(buf))
            else:
                for c in d2c[digits[di]]:
                    buf[di] = c
                    convert(di+1)
        if digits:
            convert()
        return res
