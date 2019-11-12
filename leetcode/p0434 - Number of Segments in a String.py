class Solution:
    def countSegments(self, s: str) -> int:
        res = i = 0
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            while i < len(s) and not s[i].isspace():
                i += 1
            res += 1
        return res

    def countSegments(self, s: str) -> int:
        return len(s.split())

    def countSegments(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)+1):
            if (i==len(s) or s[i].isspace()) and not s[i-1].isspace():
                res += 1
        return res
