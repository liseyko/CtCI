class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        vis = set()

        def dfs(i=0):
            if i in vis:
                return False
            if i == len(s):
                return True
            vis.add(i)
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w and\
                   dfs(i+len(w)):
                    return True
            return False

        return dfs()
