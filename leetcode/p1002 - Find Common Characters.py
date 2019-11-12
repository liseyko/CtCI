class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = collections.Counter(A[0]) if A else {}
        for w in A[1:]:
            wdic = collections.Counter(w)
            res = {k: min(res[k], wdic[k]) for k in res.keys() & wdic.keys()}
        return [k for k in res for _ in range(res[k])]
