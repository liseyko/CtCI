class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, i = 0, 1
        while i < len(s):
            if s[i] != s[i-1]:
                res, j = res + 1, i - 1
                while j > 0 and i < len(s)-1 and s[j] == s[j-1] \
                        and s[i] == s[i+1]:
                    res, i, j = res + 1, i + 1, j - 1
            i += 1

        return res

    def countBinarySubstrings(self, s):
        chunks, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        for i in range(1, len(chunks)):
            res += min(chunks[i], chunks[i - 1])
        return res
