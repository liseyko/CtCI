class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        i, j = 0, len(S)
        for c in S+S[-1]:
            if c == 'I':
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1

        return res

    def diStringMatch(self, S):
        l, r, res = 0, len(S), []
        for s in S:
            res.append(l if s == "I" else r)
            l, r = l + (s == "I"), r - (s == "D")
        return res + [l]