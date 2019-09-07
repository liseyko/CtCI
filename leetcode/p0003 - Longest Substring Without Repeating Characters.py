class Solution:
    def lengthOfLongestSubstring(self, s):
        d, res = {}, 0
        i = j = -1
        for j, c in enumerate(s):
            if c in d.keys():
                res = max(res, j-1-i) if res else j
                i = max(i, d[c])
            d[c] = j
        return max(res, j-i)


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
