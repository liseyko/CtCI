class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        substr = []
        cnt = 0
        for i, curChar in enumerate(s):
            cnt += 1
            if curChar == c:
                if res:
                    res += [i for i in range(1,cnt//2+cnt%2)]
                    res += [i for i in range(cnt//2,-1,-1)]
                else:
                    res = [i for i in range(cnt-1,-1,-1)]
                cnt = 0
        res += [i for i in range(1,cnt+1)]

        return res # if c in s else [float('inf')]*len(s)
