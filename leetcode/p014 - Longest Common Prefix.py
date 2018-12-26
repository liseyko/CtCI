class Solution(object):

    def longestCommonPrefix(self, strs):
        if not strs or not strs[0]:
            return ""
        i = -1
        while True:
            i += 1
            if i < len(strs[0]):
                c =  strs[0][i]
            for s in strs:
                if i == len(s) or c != s[i]:
                    return s[0:i]

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, c in enumerate(strs[0]):
            for w in strs[1:]:
                if i == len(w) or w[i] != c:
                    return w[:i]

        return strs[0]
