from collections import defaultdict
class Solution:
   
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)
            
        return list(res.values())

    def groupAnagrams(self, strs):
        res = defaultdict(list)
        cnt_tpl = [0] * 26
        for s in strs:
            cnt = cnt_tpl[:]
            for c in s:
                cnt[ord(c)-97] += 1
            res[tuple(cnt)].append(s)
            
        return list(res.values())
