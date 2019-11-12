class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        def dfs(buf, idxs, res, i=0):
            if i == len(idxs):
                res.append(''.join(buf))
                return
            idx = idxs[i]
            for c in (buf[idx].lower(), buf[idx].upper()):
                buf[idx] = c
                dfs(buf, idxs, res, i+1)
                
        idxs = [i for i, c in enumerate(S) if c.isalpha()]
        res = []
        dfs(list(S), idxs, res)
        return res

    def letterCasePermutation(self, S: str) -> List[str]:
        res = [list(S.lower())]
        idxs = [i for i, c in enumerate(S) if c.isalpha()]
        for i in idxs:
            buf = [w[:] for w in res]
            for w in buf:
                w[i] = w[i].upper()
                res.append(w[:])
        return [''.join(w) for w in res]

    def letterCasePermutation(self, S):
            res = [[]]
            for ch in S:
                if ch.isalpha():
                    res = [i+[j] for i in res for j in [ch.upper(), ch.lower()]]
                else:
                    res = [i+[ch] for i in res]
            return [''.join(w) for w in res]
