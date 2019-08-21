class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lookup = {word1: 1, word2: 2}
        res = len(words)
        lastword, cntr = None, 1
        for i, w in enumerate(words):
            if w not in lookup:
                if lastword:
                    cntr += 1
            else:
                if not lastword:
                    lastword = lookup[w]
                else:
                    if lastword != lookup[w]:
                        lastword = lookup[w]
                        res = min(res, cntr)
                    cntr = 1
        return res
