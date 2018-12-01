class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(r): return False
        return sorted(s) == sorted(t)

    def isAnagram(self, s, t):
        return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
    
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True    
    
    def isAnagram(self, s, t):    
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c,0) + 1
                
        for c in t:
            if c not in cnt: return False
            if cnt[c] == 1: del cnt[c]
            else: cnt[c] -= 1
        
        return not cnt