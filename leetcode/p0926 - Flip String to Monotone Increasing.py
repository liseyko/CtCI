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
    # v3
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        # count how many flip from 1 to 0
        m0=0
        
        # count how many flip from 0 to 1
        m1=0
        
        # the flag for counting 0 or 1
        isOne=False
        
        # count consecutive 0 or 1 based on isOne flag
        n=0
        for i in range(len(S)):
            if isOne:
                if S[i]=='0':
                    # flip 1->0
                    m0+=n
                    isOne=False
                    n=0
            else:
                if S[i]=='1':
                    # flip 0->1
                    m1+=n
                    # if the count of flip 1->0 is less, we should forget m1.
                    if m1>=m0:
                        m1=m0
                    isOne=True
                    n=0
            n+=1
                    
        if not isOne:
            # 0->End
            m1+=n
                
        return m0 if m0<m1 else m1 