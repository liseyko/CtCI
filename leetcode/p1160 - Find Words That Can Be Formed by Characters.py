class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        tpl = collections.Counter(chars)
        for w in words:
            wc = collections.Counter(w)
            if wc.keys() <= tpl.keys() and all(wc[k] <= tpl[k] for k in wc):
                res += len(w)
        return res
