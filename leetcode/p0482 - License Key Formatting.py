class Solution:
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
    
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res, buf = [], []

        for c in S.replace("-","").upper()[::-1]:
            buf.append(c)
            if len(buf) == K:
                res.append(''.join(buf))
                buf.clear()
                
        if buf: res.append(''.join(buf))

        return '-'.join(res)[::-1]
