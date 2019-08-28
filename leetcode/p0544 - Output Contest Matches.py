class Solution:
    def findContestMatch(self, n: int) -> str:
        res = [i+1 for i in range(n)]
        while len(res) > 1:
            for i in range(len(res)//2):
                res[i] = (res[i], res.pop())

        return str(res[0]).replace(' ','')
