class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        res, found = (0, len(s)), False
        td = collections.defaultdict(int)
        remnants = set(t)
        for c in t:
            td[c] += 1

        i = 0
        for j, c in enumerate(s):
            if c in td:
                td[c] -= 1
                if not td[c]:
                    remnants.remove(c)
                while not remnants:
                    c = s[i]
                    if c in td:
                        td[c] += 1
                        if td[c] > 0:
                            found = True
                            remnants.add(c)
                            rl = res[1]-res[0]+1
                            res = (i, j) if not rl or j-i+1 < rl else res
                    i += 1
        res = (0, -1) if not found else res
        return s[res[0]:res[1]+1]
