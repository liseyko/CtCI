class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
        res = 0
        prev = float('inf')
        for c in s:
            res += r2i[c]
            if prev < r2i[c]:
                res -= prev * 2
            prev = r2i[c]
        return res
