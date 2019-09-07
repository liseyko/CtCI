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


    def lengthOfLongestSubstring(self, s: str) -> int:
        res = j = 0
        subset = set()
        for i, c in enumerate(s):
            if c in subset:
                res = max(res, len(subset))
                while s[j] != c:
                    subset, j = subset-{s[j]}, j+1
                j += 1
            else:
                subset.add(c)
        return max(res, len(subset))
