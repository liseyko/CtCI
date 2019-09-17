class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        t = trie = {}
        res = 0
        for i in range(len(s)):
            t = trie
            substrlen = 0
            if res > len(s) - i:
                break
            for c in s[i:]:
                if c in t:
                    substrlen += 1
                else:
                    res = max(res, substrlen)
                    t[c], substrlen = {}, 0
                t = t[c]
            res = max(res, substrlen)
        #print(trie)
        return res
