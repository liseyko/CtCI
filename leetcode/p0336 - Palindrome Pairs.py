class Solution:
    """brute force"""
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def _isPal(w):
            for i in range(len(w)//2):
                if w[i] != w[~i]:
                    return False
            return True

        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if _isPal(words[i]+words[j]):
                    res.append([i, j])
                if _isPal(words[j]+words[i]):
                    res.append([j, i])
        return res
