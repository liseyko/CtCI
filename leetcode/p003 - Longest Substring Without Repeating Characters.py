class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = set()
        maxss = 0
        j = 0
        for c in s:
            if c not in ss:
                ss.add(c)
            else:
                maxss = max(maxss, len(ss))
                while s[j] != c:
                    ss.remove(s[j])
                    j += 1
                j += 1
        return max(maxss, len(ss))

    def lengthOfLongestSubstring(self, s):
        d, res = {}, 0
        i = j = -1
        for j, c in enumerate(s):
            if c in d.keys():
                res = max(res, j-1-i) if res else j
                i = max(i, d[c])
            d[c] = j
        return max(res, j-i)
