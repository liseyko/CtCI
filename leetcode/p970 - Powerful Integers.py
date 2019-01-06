class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        vals, res = {}, set()
        if bound:
            for v in (x, y):
                lim = int(math.log(bound-(x+y-v)**0, v))+1 if v > 1 else 2 - v
                vals[v] = [v**i for i in range(lim)]
            for xv in vals[x]:
                for yv in vals[y]:
                    r = xv + yv
                    if r > bound:
                        break
                    res.add(r)
        return list(res)
