class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        vis = {}
        for c in s:
            if c not in vis: 
                vis[c] = 1
            else:
                vis[c] += 1
        for i, c in enumerate(s):
            if vis[c] == 1: 
                return i
        return -1

    def firstUniqChar(self, s):
        dupe, uniq = set(), {}
        for i, c in enumerate(s):
            if c not in dupe:
                if c in uniq:
                    del uniq[c]
                    dupe.add(c)
                else:
                    uniq[c] = i
        if uniq:
            return min(uniq.values())
        return -1
