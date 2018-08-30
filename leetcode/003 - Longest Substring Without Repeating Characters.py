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
                    j+=1
                j+=1
        return max(maxss, len(ss))