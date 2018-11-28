import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wc, banned = {}, set(banned)
       
        for w in re.split("[;?!',. ]\s*", paragraph.lower().strip(";?!',. ")):
            if w in banned: continue
            if w in wc: wc[w] += 1
            else: wc[w] = 1

        return sorted(wc.items(), key = lambda x: x[1])[-1][0]

    def mostCommonWord(self, p, banned):
        banned = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]