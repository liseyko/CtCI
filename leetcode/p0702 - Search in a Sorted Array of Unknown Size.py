class Solution:
    def search(self, reader, target):
        maxlen = 2**31-1

        def bisect(li=0, ri=maxlen, tgt=target):
            if li > ri:
                return -1
            mi = li + (ri-li)//2
            m = reader.get(mi)
            if tgt < m:
                return bisect(li, mi-1)
            elif tgt > m:
                return bisect(mi+1, ri)
            return mi

        return bisect()
