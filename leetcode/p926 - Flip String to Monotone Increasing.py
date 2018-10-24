class Solution:
    # v0
    def minFlipsMonoIncr(self, S):
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in xrange(len(P)))
    # v1
    def minFlipsMonoIncr(self, S):
                    
        """
        :type S: str
        :rtype: int
        """
        l, r = {"0":0, "1":0}, {"0":0, "1":0}
        for i in range(len(S)):
            r[S[i]]+=1
        res = r["0"]            
        for i in range(len(S)):
            l[S[i]]+=1
            r[S[i]]-=1
            res = min(res, l["1"]+r["0"])
        return res