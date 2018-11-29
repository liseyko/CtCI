class Solution(object):
    def wordBreak(self, s, wordDict, i=0):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if i == len(s): return True
        
        for w in wordDict:
            wl = len(w)
            if w == s[i:i+wl]:
                if self.wordBreak(s, wordDict, i + wl):
                    return True
                
        return False

    def wordBreak(self, s, wordDict):
        cache = set()
        sl = len(s)
        self.res = False
        def bt(i=0):
            if i in cache or self.res: return
            for w in wordDict:
                wl = len(w)
                if w == s[i:i+wl]:
                    if i + wl  == sl: 
                        self.res = True
                    bt(i + wl)
            cache.add(i)
            
        bt()
        return self.res
