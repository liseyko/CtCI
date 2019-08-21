class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cw = strs[0] if strs else ""

        for i, c in enumerate(cw):
            for w in strs[1:]:
                if i == len(w) or w[i] != c:
                    return cw[:i]
        return cw
