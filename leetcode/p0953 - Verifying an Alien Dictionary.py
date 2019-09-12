class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            for i in range(max(len(w1), len(w2))):
                if i == len(w1):
                    return True
                if i == len(w2) or order[w1[i]] > order[w2[i]]:
                    return False
                elif order[w1[i]] < order[w2[i]]:
                    break
        return True

    def isAlienSorted(self, words, order):
        order = {c: i for i, c in enumerate(order)}
        nwords = [[order[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(nwords, nwords[1:]))
