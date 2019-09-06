class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        tl = text.split()
        for i in range(len(tl)-2):
            if tl[i] == first and tl[i+1] == second:
                res.append(tl[i+2])
        return res
