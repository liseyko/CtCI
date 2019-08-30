class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        snk = ('0', '1', '8', '6', '9')
        sn = {
              '0': '0',
              '1': '1',
              '8': '8',
              '6': '9',
              '9': '6',
             }
        res = []
        halfres = []
        def bt(s=[]):
            if len(s) == n//2:
                halfres.append(s[:])
                return
            keys = snk if s else snk[1:]
            for c in keys:
                bt(s+[c])
        bt()
        for i, rec in enumerate(halfres):
            inversion = []
            for c in rec[::-1]:
                inversion.append(sn[c])
            if n % 2 == 0:
                res.append(''.join(rec+inversion))
            else:
                for c in snk[:3]:
                    res.append(''.join(rec+[sn[c]]+inversion))

        return res
