class Solution:
    def _getCenter(self, sc):
        center = []
        for c, q in sc.items():
            if q%2 == 1:
                center.append(c)
        return center


    def generatePalindromes(self, s: str) -> List[str]:
        sc = collections.Counter(s)
        center = self._getCenter(sc)
        if center:
            if len(center) > 1:
                return []
            sc[center[0]] -= 1

        perms = []

        def bt(cnt=sum(sc.values()), buf=[]):
            if not cnt:
                perms.append(buf[:])
                return
            for c in sc:
                if not sc[c]:
                    continue
                sc[c] -= 2
                bt(cnt-2, buf+[c])
                sc[c] += 2

        bt()

        return [''.join(w[::-1]+center+w) for w in perms]
