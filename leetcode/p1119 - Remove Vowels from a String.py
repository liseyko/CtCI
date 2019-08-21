class Solution:
    def removeVowels(self, S: str) -> str:
        S=list(S)
        skip = set(['a', 'e', 'i', 'o', 'u'])
        offset = 0
        for i, c in enumerate(S):
            if c in skip:
                continue
            if i != offset:
                S[offset] = c
            offset += 1
        return ''.join(S[:offset])
