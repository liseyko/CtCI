import re


class Solution:
    def mostCommonWord(self, p, banned):
        banned = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned) | {''}
        wc = collections.defaultdict(int)
        topCntWrd = (0, None)
        for w in re.split('[ ,.;:!?"\']', paragraph.lower()):
            if w in banned:
                continue
            wc[w] += 1
            topCntWrd = max(topCntWrd, (wc[w], w))
        return topCntWrd[1]
