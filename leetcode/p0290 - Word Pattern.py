class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        lst = str.split()
        if len(pattern) != len(lst):
            return False
        for i, c in enumerate(pattern):
            if c not in d and lst[i] not in d.values():
                d[c] = lst[i]
            if d.get(c, None) != lst[i]:
                return False
        return True
