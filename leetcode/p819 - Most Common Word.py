import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wc = {}
        for w in re.split('[\';?!,. ]\s*', paragraph.lower()):
            if not w or w in banned: continue
            if w in wc: wc[w] += 1
            else: wc[w] = 1
        #print(sorted(wc.items(), key = lambda x: x[1]))
        
        
        return sorted(wc.items(), key = lambda x: x[1])[-1][0]