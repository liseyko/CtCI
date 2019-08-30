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
            inversion = [sn[c] for c in rec[::-1]]
            if n % 2 == 0:
                res.append(''.join(rec+inversion))
            else:
                for c in snk[:3]:
                    res.append(''.join(rec+[sn[c]]+inversion))

        return res


    def findStrobogrammatic(self, n: int) -> List[str]:
        sn = [['0', '1', '8'],
              ['11', '88', '69', '96', '00']]
        if n == 1:
            return sn[0]
        elif n == 2:
            return sn[1][:-1]
        else:
            prev = self.findStrobogrammatic(n-1-(n+1)%2)
            res = []
            for ins in sn[(n+1)%2]:
                for num in prev:
                    prevMidIdx = (n-1)//2
                    res.append(''.join(num[:prevMidIdx]+ins+num[prevMidIdx:]))
            return res
