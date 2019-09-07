class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = subres = 0
        for i, c in enumerate(s):
            if c in d:
                res = max(res, subres)
                subres = min(subres, i-d[c]-1)
            subres += 1
            d[c] = i
        return max(res, subres)
